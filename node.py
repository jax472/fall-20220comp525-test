class Node:
    """
    Class representation of a Node
    """

    def __init__(self, data):
        """
        Constructor
        :param data: the data to place in the node
        :type data: any
        """
        self._data = data
        self._next = None

    def get_data(self):
        """
        Getter for the node data
        :return: the data
        :rtype: any
        """
        return self._data

    def get_next(self):
        """
        Gett for the node next
        :return: the next node
        :rtype: Node || None
        """
        return self._next

    def set_data(self, data):
        """
        Setter for the data
        :param data: the new data
        :type data: any
        """
        self._data = data

    def set_next(self, next_node):
        """
        Setter for the next
        :param next_node: next node
        :type next_node: Node || None
        """
        self._next = next_node