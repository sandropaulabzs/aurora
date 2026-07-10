from abc import ABC, abstractmethod


class System(ABC):
    """
    Classe base para todos os sistemas da SEED Engine.
    """

    @abstractmethod
    def update(self) -> None:
        """
        Executa uma atualização do sistema.
        """
        pass