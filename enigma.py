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
        alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

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
            self.rotor1 = dict(zip(alphabet, I))
            self.rotor2 = dict(zip(alphabet, II))
            self.rotor3 = dict(zip(alphabet, III))
            # TODO did this also rotate ever?
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

    def encode(plaintext):
        return None

    def decode(cyphertext):
        return None
