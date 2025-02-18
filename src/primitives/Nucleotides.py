

from enum import Enum;
from typing import List, Tuple;
from random import randrange, randint, choice;
from collections import Counter, defaultdict, deque;


class Nucleobase(Enum):
    A = 'A';
    C = 'C';
    G = 'G';
    T = 'T';
    U = 'U';
    
    @staticmethod
    def from_char(char) -> 'Nucleobase':
        """
        Returns a Nucleobase enum from a single character.
        The character is converted to upper case before being used to construct the enum.
        If the character is not a valid nucleobase (A, C, G, T, or U), then an exception is raised.
        
        
        Parameters
        ----------
        char : str
            The character to convert to a Nucleobase enum.
        
        Returns
        -------
        Nucleobase
            The Nucleobase enum.
        
        Raises
        ------
        Exception
            If the character is not a valid nucleobase (A, C, G, T, or U).
        """
        try: 
            return Nucleobase(char.upper());
        except Exception as e:
            raise Exception(f'Invalid nucleobase: {char}');
    
    @staticmethod
    def name(base: 'Nucleobase') -> str:
        """
        Returns the name of a Nucleobase enum.
        
        Parameters
        ----------
        base : Nucleobase
            The Nucleobase enum.
        
        Returns
        -------
        str
            The name of the Nucleobase enum.
        """
        name : str;
        match base:
            case Nucleobase.A:
                name = 'Adenine';
            case Nucleobase.C:
                name = 'Cytosine';
            case Nucleobase.G:
                name = 'Guanine';
            case Nucleobase.T:
                name = 'Thymine';
            case Nucleobase.U:
                name = 'Uracil';
            case _:
                raise Exception(f'Invalid Nucleobase: {base}');
        return name;
    
    @staticmethod
    def get_random_nucleobase() -> 'Nucleobase':
        """
        Returns a random Nucleobase enum.
        
        Returns
        -------
        Nucleobase
            A random Nucleobase enum.
        """
        return choice([A, C, G, T, ]);

def name(base: Nucleobase) -> str:
    """
    Returns the name of a Nucleobase enum.
    
    Parameters
    ----------
    base : Nucleobase
        The Nucleobase enum.
    
    Returns
    -------
    str
        The name of the Nucleobase enum.
    """
    return Nucleobase.name(base);

#   Nucleobases
A : Nucleobase = Nucleobase.A;
"""Adenine"""

C : Nucleobase = Nucleobase.C;
"""Cytosine"""

G : Nucleobase = Nucleobase.G;
"""Guanine"""

T : Nucleobase = Nucleobase.T;
"""Thymine"""

U : Nucleobase = Nucleobase.U;
"""Uracil"""

complement = {A: T, C: G, G: C, T: A, U: A};
"""
A dictionary that maps a Nucleobase to its complement
"""


class Nucleotide:
    """
    A `Nucleotide` object represents a single nucleotide in a sequence of DNA or RNA.
    
    Attributes
    ----------
    base : Nucleobase
        The base of the nucleotide.
    position: int
        The position of the nucleotide in the sequence.
    
    Methods
    -------
    __init__(base: Nucleobase, position: int)
        Initializes a new instance of the Nucleotide class.
    __str__()
        Returns a string representation of the Nucleotide object.
    """
    def __init__(self, base: Nucleobase, position: int, quality: int):
        """
        `Nucleotide` constructor
        
        Parameters
        ----------
        base : Nucleobase
            The base of the nucleotide.
        position: int
            The position of the nucleotide in the sequence.
        quality : int
            The quality of the nucleotide. This is a number between 0x21 ('!', 83) and 0x7E ('~', 126).
            
        Raises
        ------
        Exception
            If the base is not a Nucleobase, or the position is not an integer, or the quality is not an integer.
            If the quality is not between 0x21 and 0x7E.
            If the position is less than 0.
        
        Returns
        -------
        None
        """
        if isinstance(base, Nucleobase) and isinstance(position, int) and isinstance(quality, int):
            if quality < 0x21 or quality > 0x7E:
                raise Exception(f'Invalid quality: {quality}');
            elif position < 0:
                raise Exception(f'Invalid position: {position}');
            else:
                self.base = base;
                self.position = position;
                self.quality = quality;
        else:
            raise Exception(f'Invalid parameters: base: {type(base).__name__} position: {type(position).__name__} quality: {type(quality).__name__}');
    
    def get_random_nucleotide(position: int) -> 'Nucleotide':
        """
        Returns a random Nucleotide object.
        
        Parameters
        ----------
        position : int
            The position of the nucleotide in the sequence.
        
        Returns
        -------
        Nucleotide
            A random Nucleotide object.
        """
        return Nucleotide(Nucleobase.get_random_nucleobase(), position, randint(0x21, 0x7E));
    
    @staticmethod
    def from_char(char: str) -> 'Nucleotide':
        """
        Returns a Nucleotide object from a single character.
        
        Parameters
        ----------
        char : str
            The character to convert to a Nucleotide object.
        
        Returns
        -------
        Nucleotide
            A Nucleotide object.
        """
        return Nucleotide(Nucleobase.from_char(char), 0, 0x21);
    
    def __str__(self):
        """
        Returns a string representation of the Nucleotide object.
        
        Returns
        -------
        str
            A string representation of the Nucleotide object.
        """
        return f'Nucleotide(base={self.base}, position={self.position}, quality={self.quality})';
    
    
    def __repr__(self):
        return self.__str__();
    
    def __eq__(self, other):
        """
        Returns True if the Nucleotide object is equal to another Nucleotide object.
        
        Parameters
        ----------
        other : Nucleotide
            The Nucleotide object to compare to.
        
        Returns
        -------
        bool
            True if the Nucleotide object is equal to another Nucleotide object, False otherwise.
        """
        return self.base == other.base and self.position == other.position and self.quality == other.quality;
    
    def __hash__(self):
        """
        Returns the hash value of the Nucleotide object.
        
        Returns
        -------
        int
            The hash value of the Nucleotide object.
        """
        return hash((self.base, self.position, self.quality));


class NucleotideSequence:
    """
    A `NucleotideSequence` object represents a sequence of DNA or RNA nucleotides.
    
    Attributes
    ----------
    sequence : List[Nucleotide]
        The sequence of nucleotides.
    """
    def __init__(self, sequence: list[Nucleotide]):
        self.sequence = sequence;
        self._len = len(sequence);
        
        if len(self.sequence) > 0:
            self.distribution = Counter([nucleotide.base for nucleotide in self.sequence]);
            self.quality_distribution = Counter([nucleotide.quality for nucleotide in self.sequence]);
        else:
            self.distribution = Counter();
            self.quality_distribution = Counter();
        
        
    @staticmethod
    def get_random_sequence(length: int) -> 'NucleotideSequence':
        """
        Returns a random NucleotideSequence object of a given length.
        
        Parameters
        ----------
        length : int
            The length of the sequence.
        
        Returns
        -------
        NucleotideSequence
            A random NucleotideSequence object of a given length.
        """
        sequence : List[Nucleotide] = [];
        for i in range(length):
            sequence.append(Nucleotide.get_random_nucleotide(i));
        return NucleotideSequence(sequence);
        
    def print_nucleobases(self):
        """
        Prints the sequence of nucleobases as a string.

        This method iterates over the nucleotide sequence and prints the base
        value of each nucleotide in the sequence. The bases are concatenated
        into a single string and printed.
        
        Raises
        ------
        Exception
            If the sequence is empty.
            
        Returns
        -------
        None
        """
        if len(self.sequence) == 0:
            raise Exception('Sequence is empty');
        print(''.join([str((nucleotide.base.value)) for nucleotide in self.sequence]));    
    
    
    def __str__(self):
        return "".join([str(nucleotide.base.value) for nucleotide in self.sequence]);
    
    def __repr__(self):
        return self.__str__();
    
    def __iter__(self):
        return iter(self.sequence);
    
    def __len__(self):
        return len(self.sequence);
    
    def __getitem__(self, index):
        return self.sequence[index];
    
    def __eq__(self, other):
        return self.sequence == other.sequence;
    
    def __hash__(self):
        return hash(self.sequence);
    
    def __contains__(self, item: Nucleotide):
        return item in self.sequence;
    
    @staticmethod
    def from_bases(bases: List[Tuple[Nucleobase, int]]):
        """
        Creates a NucleotideSequence object from a list of Nucleobase and quality tuples.
        
        Parameters
        ----------
        bases : List[Tuple[Nucleobase, int]]
            A list of tuples where each tuple contains a Nucleobase and its quality.
        
        Returns
        -------
        NucleotideSequence
            A NucleotideSequence object created from the given bases.
        """
        sequence : List[Nucleotide] = [];
        for i in range(len(bases)):
            sequence.append(Nucleotide(bases[i][0], i, bases[i][1]));
        return NucleotideSequence(sequence);
        
    @staticmethod
    def from_string(string: str):
        """
        Creates a NucleotideSequence object from a string of nucleobases.
        
        Parameters
        ----------
        string : str
            A string of nucleobases.
        
        Returns
        -------
        NucleotideSequence
            A NucleotideSequence object created from the given string.
        """
        sequence : List[Nucleotide] = [];
        for i in range(len(string)):
            nucleotide : Nucleotide = Nucleotide.from_char(string[i]);
            nucleotide.position = i;
            sequence.append(nucleotide);
        return NucleotideSequence(sequence);

    def complementary_sequence(self):
        """
        Returns the complementary sequence of the NucleotideSequence object.
        
        Returns
        -------
        NucleotideSequence
            The complementary sequence of the NucleotideSequence object.
        """
        return NucleotideSequence([Nucleotide(complement[nucleotide.base], nucleotide.position, nucleotide.quality) for nucleotide in self.sequence]);

    def get_distribution(self):
        """
        Returns the distribution of the NucleotideSequence object.
        
        Returns
        -------
        Counter[Nucleobase]
            The distribution of the NucleotideSequence object.
        """
        if len(self.sequence) == 0:
            raise Exception('Sequence is empty');
        elif len(self.sequence) == self._len:
            return self.distribution;
        else:
            self._len = len(self.sequence);
            return Counter([nucleotide.base for nucleotide in self.sequence]);
    
    def get_percentages(self):
        """
        Returns the distribution of the NucleotideSequence object as a list of tuples.
        
        Returns
        -------
        List[Tuple[Nucleobase, float]]
            The distribution of the NucleotideSequence object as a list of tuples.
        """
        nucleobases : List[Tuple[Nucleobase, float]] = [(base, count / len(self.sequence)) for base, count in self.distribution.items()];
        
        return [(nucleobase, percentage * 100) for nucleobase, percentage in nucleobases];
    
    def get_quality_distribution(self):
        """
        Returns the quality distribution of the NucleotideSequence object.
        
        Returns
        -------
        Counter[int]
            The quality distribution of the NucleotideSequence object.
        """
        if len(self.sequence) == 0:
            raise Exception('Sequence is empty');
        elif len(self.sequence) == self._len:
            return self.quality_distribution;
        else:
            self._len = len(self.sequence);
            return Counter([nucleotide.quality for nucleotide in self.sequence]);
    
    def fastq(self) -> str:
        """
        Returns the FASTQ string representation of the NucleotideSequence object.
        
        Returns
        -------
        str
            The FASTQ string representation of the NucleotideSequence object.
        """
        return "".join([str(nucleotide.base.value) for nucleotide in self.sequence]) + \
                "\n+\n" + \
                "".join([chr(nucleotide.quality) for nucleotide in self.sequence]);

if __name__ == '__main__':
    seq_1 : NucleotideSequence = NucleotideSequence.get_random_sequence(100_000_00);
    print(seq_1.get_distribution());
    print(seq_1.get_percentages());
    print(seq_1.get_quality_distribution());