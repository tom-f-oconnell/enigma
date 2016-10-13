#!/usr/bin/env python3

"""
Much of the historical facts in the comments came from the
'Enigma rotor details' Wikipedia page.
"""

import random

class Enigma:
    """ Encodes text as an enigma would. 
        Can work as Enigma I, M3 Army, or M3 & M4 Naval machine. """

    def __init__(self, model='Enigma I'):

        # TODO rotor settings and plugboard. 4th rotor? else?

        # TODO maybe move all this stuff out of init?
        self.alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

        # rotors from the Enigma I
        # introduced in 1930
        I = 'EKMFLGDQVZNTOWYHXUSPAIBRCJ'
        II = 'AJDKSIRUXBLHWTMCQGZNPYFVOE'
        III = 'BDFHJLCPRTXVZNYEIWGAKMUSQO'

        # additional possible rotors for the M3 Army enigma
        IV = 'ESOVPZJAYQUIRHXLNFTGKDCMWB'
        V = 'VZBRGITYUPSDNHLXAWMJQOFECK'

        # additional possible rotors for the M3 & M4 Naval (FEB 1942)
        VI = 'JPGVOUMFYQBENHZRDKASXLICTW'
        VII = 'NZJHGRCXMYSWBOUFAIVLPEKQDT'
        VIII = 'FKQHTLXOCBJSPDZRAMEWNIUYGV'

        # not sure which reflectors were most common
        # seems maybe "wide" reflector B, for a while

        # M4 R2
        beta = 'LEYJVCNIXWPBQMDRTAKZGFUHOS'
        gamma = 'FSOKANUERHMBTIYCWLQPZXVGJD'

        # ?
        a = 'EJMZALYXVBWFCRQUONTSPIKHGD'
        b = 'YRUHQSLDPXNGOKMIEBFZCWVJAT'
        c = 'FVPJIAOYEDRZXWGCTKUQSBNMHL'

        # M4 R1 (M3 + thin)
        b_thin = 'ENKQAUYWJICOPBLMDXZVFTHRGS'
        c_thin = 'RDOBJNTKVEHMLFCWZAXGYIPSUQ'

        # used on the Enigma I (it seems?)
        etw = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

        mk2 = {2, 'M3 Army', 'Army'}
        mk3 = {3, 'M3 & M4 Naval', 'M4 Naval', 'M4', 'Naval'}

        if model == 'Enigma I' or model == 1:
            self.rotor1 = I
            self.rotor2 = II
            self.rotor3 = III
            
            # go between 0 and len(rotor) - 1
            self.offset1 = 0
            self.offset2 = 0
            self.offset3 = 0

            self.reflector = etw

            self.turn2 = I[0]
            self.turn3 = II[0]

        elif model in mk2 or model in mk3:

            if model in mk2:
                possible_rotors = [I, II, III, IV, V]
                self.reflector = b
                        
            else:
                possible_rotors = [I, II, III, IV, V, VI, VII, VIII]
                # ?
                self.reflector = beta

            n_rotors = 3
            rotors = random.sample(possible_rotors, n_rotors)
            self.rotor1 = rotors[0]
            self.rotor2 = rotors[1]
            self.rotor3 = rotors[2]

            # the first rotor spins unconditionally
            # turns the second rotor if the first rotor reaches its first position again
            self.turn2 = rotors[0][0]
            # likewise for third rotor
            # TODO might need two turn points for the M4
            self.turn3 = rotors[1][0]

        else:
            raise NameError('unrecognized enigma model')

    def mapchar(self, char, from_string, to_string):
        # TODO don't linear scan
        char = char.upper()
        for i, c in enumerate(from_string):
            if c == char:
                return to_string[i]

        raise NameError('character not in string maps')
    
    def encode_char(self, char):
        r1_in = self.mapchar(char, self.alphabet, self.rotor1)
        r2_in = self.mapchar(r1_in, self.rotor1, self.rotor2)
        r3_in = self.mapchar(r2_in, self.rotor2, self.rotor3)

        ref_out = self.mapchar(r3_in, self.rotor3, self.reflector)

        r1_out = self.mapchar(ref_out, self.alphabet, self.rotor1)
        r2_out = self.mapchar(r1_out, self.rotor1, self.rotor2)
        encoded = self.mapchar(r2_out, self.rotor2, self.rotor3)

        # TODO precedence?
        # circularly shift the rotor (as if spinning it)
        self.rotor1 = self.rotor1[1:] + self.rotor1[0]
        
        if self.rotor1[0] == self.turn2:
            self.rotor2 = self.rotor2[1:] + self.rotor2[0]

        # TODO or 'in' if not unique
        if self.rotor2[0] == self.turn3:
            self.rotor3 = self.rotor3[1:] + self.rotor3[0]

        return encoded

    def encode(self, plaintext):
        return ''.join([self.encode_char(x) for x in plaintext])

    def decode(self, cyphertext):
        return None
