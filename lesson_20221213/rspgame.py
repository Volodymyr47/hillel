from abc import ABC, abstractmethod
from rich.console import Console
from rich.prompt import Prompt
import random
import socket


rc = Console()


class Player(ABC):
    """
    Abstract class for create a new Player
    """
    _name = None
    _selected_figure = None
    _score = 0

    @abstractmethod
    def __init__(self):
        """
        Abstract magic method of class Player
        """
        pass

    @abstractmethod
    def select_figure(self, item):
        """
        Abstract method of class Player for selecting figure by player.
        Args:
            item: type Figure.

        Returns: None
        """
        pass

    @property
    def selected_figure(self):
        return self._selected_figure

    def increase_score(self):
        """
        Common method for all Players. Use to increase player's score
        Returns: None
        """
        self._score += 1

    def reset_score(self):
        """
        Reset scores (_score = 0)
        Returns: None
        """
        self._score = 0

    @abstractmethod
    def get_score(self):
        pass

    def __str__(self):
        """
        A string representation of a Figure class object
        Returns: string - name of Player class object

        """
        return self._name

    def __eq__(self, other):
        """
        Comparison of players by their account
        Args:
            other: other instance of Player. Type Player
        Returns: bool

        """
        return self.get_score() == other.get_score()

    def __ne__(self, other):
        """
        Comparison of players by their account
        Args:
            other: other instance of Player. Type Player
        Returns: bool

         """
        return self.get_score() != other.get_score()

    def __gt__(self, other):
        """
        Comparison of players by their account
        Args:
            other: other instance of Player. Type Player
        Returns: bool

        """
        return self.get_score() > other.get_score()

    def __ge__(self, other):
        """
        Comparison of players by their account
        Args:
            other: other instance of Player. Type Player
        Returns: bool

        """
        return self.get_score() >= other.get_score()

    def __lt__(self, other):
        """
        Comparison of players by their account
        Args:
            other: other instance of Player. Type Player
        Returns: bool

        """
        return self.get_score() < other.get_score()

    def __le__(self, other):
        """
        Comparison of players by their account
        Args:
            other: other instance of Player. Type Player
        Returns: bool

        """
        return self.get_score() <= other.get_score()


class HumanPlayer(Player):
    _selected_figure = None
    _name = None
    _score = 0

    def __init__(self, name):
        """
        Initializing instance of class HumanPlayer.
        Args:
            name: string. Name is a name of the player
        """
        self.player_name = name

    @property
    def player_name(self):
        """
        Property of player name
        Returns: string. Name of the HumanPlayer class object

        """
        return self._name

    @player_name.setter
    def player_name(self, value):
        """
        Name-Setter of the HumanPlayer object name
        Args:
            value: string

        Returns: None

        """
        if not isinstance(value, str):
            raise TypeError(f'The type of {value} must be a string')
        if value == '':
            self._name = 'Human player'
        else:
            self._name = value.capitalize()

    def select_figure(self, item):
        """
        The method of selecting and assigning an item to _selected_figure variable for human player
        Args:
            item: type Figure

        Returns: None

        """
        if not isinstance(item, Figure):
            raise TypeError(f'The type of {item} must be a Figure')
        self._selected_figure = item

    def get_score(self):
        """
        The method to getting human player score
        Returns: int

        """
        return self._score


class VirtualPlayer(Player):
    _selected_figure = None
    _name = None

    def __init__(self, name):
        """
        Initializing instance of the class HumanPlayer
        Args:
            name: Type string. Name is a name of the player
        """
        self.player_name = name

    @property
    def player_name(self):
        """
        Property of player name
        Returns: string. Name of the VirtualPlayer class object

        """
        return self._name

    @player_name.setter
    def player_name(self, value):
        """
       Name-Setter of the VirtualPlayer object name
        Args:
            value: string

        Returns: None

        """
        if not isinstance(value, str):
            raise TypeError(f'The type of {value} must be a string')
        if value == '':
            self._name = socket.gethostname().capitalize()
        else:
            self._name = value.capitalize()

    def select_figure(self, items):
        """
        The method of selecting and assigning an item to _selected_figure variable for virtual player.
        Works with random choice

        Args:
        items: type Figure

        Returns: None

        """
        self._selected_figure = random.choice(items)

    def get_score(self):
        """
        The method to getting virtual player score
        Returns: int

        """
        return self._score


class Figure:
    _name = None
    priority = None
    index = 0

    def __init__(self, name):
        """
        Initializing instance of class HumanPlayer.
        Args:
            name: Type string. Name - name of figure

        """
        self.name = name
        if self.name == 'rock'.capitalize():
            self.index = 1
            self.priority = '132'
        if self.name == 'scissors'.capitalize():
            self.index = 2
            self.priority = '213'
        if self.name == 'paper'.capitalize():
            self.index = 3
            self.priority = '321'

    @property
    def name(self):
        """
        Property of figure name
        Returns: string. Name of the Figure class object

        """
        return self._name

    @name.setter
    def name(self, value):
        """
        Name-Setter of the Figure object name
        Args:
            value: string

        Returns: None

        """
        if not isinstance(value, str):
            raise TypeError(f'The type of {value} must be a string')
        self._name = value.capitalize()

    def __str__(self):
        """
        A string representation of a Figure class object
        Returns:

        """
        return self._name

    def __eq__(self, other):
        """
        Comparison of players by their account
        Args:
            other: other instance of Player. Type Player
        Returns: bool. Return True if self figure is equal other figure by priority

        """
        return int(self.priority[other.index - 1]) == int(other.priority[self.index - 1])

    def __ne__(self, other):
        """
        Comparison of players by their account
        Args:
            other: other instance of Player. Type Player
        Returns: bool. Return True if self figure is not equal other figure by priority

        """
        return int(self.priority[other.index - 1]) != int(other.priority[self.index - 1])

    def __gt__(self, other):
        """
        Comparison of players by their account
        Args:
            other: other instance of Player. Type Player
        Returns: bool. Return True if self figure is greater other figure by priority

        """
        return int(self.priority[other.index - 1]) > int(other.priority[self.index - 1])

    def __ge__(self, other):
        """
        Comparison of players by their account
        Args:
            other: other instance of Player. Type Player
        Returns: bool. Return True if self figure is greater or equal other figure by priority

        """
        return int(self.priority[other.index - 1]) >= int(other.priority[self.index - 1])

    def __lt__(self, other):
        """
        Comparison of players by their account
        Args:
            other: other instance of Player. Type Player
        Returns: bool. Return True if self figure is lester other figure by priority

        """
        return int(self.priority[other.index - 1]) < int(other.priority[self.index - 1])

    def __le__(self, other):
        """
        Comparison of players by their account
        Args:
            other: other instance of Player. Type Player
        Returns: bool. Return True if self figure is lester or equal other figure by priority

        """
        return int(self.priority[other.index - 1]) <= int(other.priority[self.index - 1])


class Rule:
    player1 = None
    player2 = None

    def __init__(self, player1, player2):
        """
        Initializing instance of class Rule.
        Args:
            player1: Player. The instance of HumanPlayer or VirtualPlayer class
            player2: Player. The instance of HumanPlayer or VirtualPlayer class

        """
        self.player1 = player1
        self.player2 = player2

    def round_winner(self):
        """
        Get the winner of the one game round
        Returns: Player - return instance of HumanPlayer or VirtualPlayer
        """
        if self.player1.selected_figure > self.player2.selected_figure:
            self.player1.increase_score()
            return self.player1
        if self.player2.selected_figure > self.player1.selected_figure:
            self.player2.increase_score()
            return self.player2

    def game_winner(self):
        """
        Get the winner of the game
        Returns: Player - return instance of HumanPlayer or VirtualPlayer

        """
        if self.player1 > self.player2:
            return self.player1

        if self.player2 > self.player1:
            return self.player2


class MainGame:
    _player = None
    _is_human = None
    rule = None

    def __init__(self, player: str, *, is_human: int):
        """
        Initializing instance of class MainGame.
        Args:
            player: string - player name.
            is_human: int - 0 (VirtualPlayer) or 1 (HumanPlayer)
        """
        self.is_human = is_human
        self.player = player

    @property
    def is_human(self):
        """
        The property of the player type
        Returns: int - player type. If 0 - virtual player, if 1 - human player

        """
        return self._is_human

    @is_human.setter
    def is_human(self, value):
        """
        Player-type setter
        Args:
            value: int
        Returns: None

        """
        if value not in (0, 1):
            raise ValueError(f'The Value of {value} must be 1 (is Human) or 0 (is not Human, is Virtual)')
        self._is_human = value

    @property
    def player(self):
        """
        The property of the player
        Returns: string - player name

        """
        return self._player

    @player.setter
    def player(self, name):
        """
        Player-setter.
        Args:
            name: string - player name

        Returns: None

        """
        if self._is_human == 1:
            self._player = HumanPlayer(name)
        else:
            self._player = VirtualPlayer(name)

    def choose_figure(self):
        """
        The method of defining shapes and selecting a shape by the player
        Also this method give control to choose figure human player or virtual player
        Returns: None

        """
        rock = Figure('rock')
        scissors = Figure('scissors')
        paper = Figure('paper')
        figures = (rock, scissors, paper)

        rc.print(f'\n{self.player}, you have to choose your figure')
        if self.is_human == 0:
            self.player.select_figure(figures)
        else:
            figure_index = Prompt.ask('Please, make your choice',
                                      choices=['1', '2', '3'],
                                      show_choices=False)
            self.player.select_figure(figures[int(figure_index) - 1])

    def start(self, other):
        """
        The method starts the game and check what figure the player has selected in the round.
        After that method will print information abot the player figure of the one game round
        Args:
            other: instance of Player - other game player

        Returns: Player (HumanPlayer or VirtualPlayer) - the round winner

        """
        self.choose_figure()
        other.choose_figure()

        if self.player.selected_figure:
            print(f'\nThe {self.player.player_name}\'s figure is {self.player.selected_figure}')

        if other.player.selected_figure:
            print(f'The {other.player.player_name}\'s figure is {other.player.selected_figure}')

        self.rule = Rule(self.player, other.player)
        round_winner = self.rule.round_winner()
        return round_winner

    def play_game(self, other, iterations):
        """
        Whole game control method: with iterations and return the winner
        Args:
            other: type Player - instance of HumanPlayer or VirtualPlayer
            iterations: int - count of game iterations

        Returns: string - winner player name

        """

        self.player.reset_score()
        other.player.reset_score()

        if iterations:
            if iterations < 1:
                raise ValueError(f'The value of iterations must be > 0. We have got the value {iterations}')
        else:
            iterations = 3
            print(f'Count of iterations is {iterations}')

        i = 1
        while i <= iterations:
            print(f'\nRound {i}')
            self.start(other)
            i += 1
        result_game = Rule(self.player, other.player).game_winner()
        return result_game
