import ipaddress as ipa


class Router:

    def __init__(self):
        """Конструктор класса Router.
        Каждому объекту класса назначается устройство lo.
        """
        self.interface = {'lo': ipa.IPv4Interface('127.0.0.1/8')}
        self.routes = {'lo': {self.interface['lo'].network: '127.0.0.1'}}

    def addIP(self, new_interface, new_address):
        """ добавляет новый IP.

        :param new_interface: устройство, на которое вешается адрес (eth0, eth1 ...)
        :param new_address: IP адрес (192.168.5.14/24)
        :return: в словарь interface добавляет новое устройство и его адрес (eth0: 192.168.5.14/24)
                 в словарь routes добавляет маршрут к подсети в пространстве которого находится адрес

        Example:
        >>> a = Router()
        >>> a.addIP('eth0', '192.168.5.14/24')
        >>> a.addIP('eth1', '192.168.5.14/24')

        eth0:192.168.5.14/24 successful added
        eth1: 192.168.5.14/24 already exist
        """
        if ipa.IPv4Interface(new_address) not in self.interface.values():
            self.interface[new_interface] = ipa.IPv4Interface(new_address)  # создание нового IP адреса
            self.routes[new_interface] = {self.interface[new_interface].network:  # добавление маршрута
                                          list(ipa.ip_network(self.interface[new_interface].network).hosts())[0]}
            print(f"{new_interface}:{new_address} successful added")
        else:
            print(f"{new_interface}: {new_address} already exist")

    def removeIP(self, rem_interface, rem_address):
        """удаление IP.

        :param rem_interface: устройство, на котором висит адрес (eth0, eth1 ...)
        :param rem_address: IP адрес (192.168.5.14/24)
        :return: из словаря interface добавляет устройство и его адрес (eth0: 192.168.5.14/24)
                 из словаря routes удаляет маршрут к подсети в пространстве которого находится адрес

        Если устройство rem_interface зарегистрировано в interface и к этому устройству привязан rem_address,
        то сначала удаляется удаляется маршрут, а затем адрес.

        Example:
        >>> a = Router()
        >>> a.addIP('eth0', '192.168.5.14/24')
        >>> a.removeIP('eth0', '192.168.5.14/24')
        >>> a.removeIP('eth1', '192.168.6.14/24')

        eth0:192.168.5.14/24 removed
        eth1:192.168.6.14/24 doesn't exist
        """
        if rem_interface in self.interface.keys() and self.interface[rem_interface] == ipa.IPv4Interface(rem_address):
            self.removeRoute(rem_interface)
            self.interface.pop(rem_interface)
            print(f"{rem_interface}:{rem_address} removed")
        else:
            print(f"{rem_interface}:{rem_address} doesn't exist")

    def getListIP(self):
        """Выводит список IP адресов.

        Example:
        >>> a = Router()
        >>> a.addIP('eth0', '192.168.5.14/24')
        >>> a.getListIP()

        eth0:192.168.5.14/24 successful added
        IP addresses:
        lo:	address	127.0.0.1 netmask	255.0.0.0 network	127.0.0.0/8
        eth0:	address	192.168.5.14 netmask	255.255.255.0 network	192.168.5.0/24
        """
        print(f"IP addresses:")
        for i in self.interface.keys():
            print(f"{i}:\t"
                  f"address\t{self.interface[i].ip} "
                  f"netmask\t{self.interface[i].netmask} "
                  f"network\t{self.interface[i].network}")

    def addRoute(self, target_network, gateway):
        """Добавляет маршрут в таблицу маршрутизации.

        :param target_network: адрес цели (192.168.22.0/24)
        :param gateway: шлюз в локальной сети, через который можно достичь этого адреса (192.168.5.20)
        :return: если gateway доступен в таблице маршрутизации (то есть в routes), тогда в словарь routes добавляется
        маршрут к target_network через указанный gateway

        Example:
        >>> a = Router()
        >>> a.addIP('eth0', '192.168.5.14/24')
        >>> a.addRoute('192.168.22.0/24', '192.168.5.20')
        >>> a.addRoute('192.168.33.0/24', '192.168.11.20')

        eth0:192.168.5.14/24 successful added
        Route to 192.168.22.0/24 via 192.168.5.20 successful added
        Exception: you cannot set such a route!!!
        """
        for key in self.routes.keys():
            if key != 'lo':
                for k in self.routes[key].keys():
                    if ipa.ip_address(gateway) in list(k.hosts()):  # проверка доступа к gateway в таблице маршрутизации
                        self.routes[key][ipa.IPv4Interface(target_network).network] = ipa.ip_address(gateway)
                        return print(f"Route to {target_network} via {gateway} successful added")
                    else:
                        return print(f"Exception: you cannot set such a route!!!")

    def removeRoute(self, rem_interface, rem_network=None):
        """Удаляет маршрут из таблицы маршрутизации

        :param rem_interface: устройство, на котором висит адрес (eth0, eth1 ...) для доступа rem_network
        :param rem_network: сеть, доступ к которой необходимо удалить
        :return: Если при вызове не указывается rem_network, тогда выполняется удаление всех маршрутов, проходящие
        через устройство rem_interface. В другом случае выполняется удаление rem_network с устройства rem_interface

        Example:
        >>> a = Router()
        >>> a.addIP('eth0', '192.168.5.14/24')
        >>> a.addRoute('192.168.22.0/24', '192.168.5.20')
        >>> a.getListRoute()
        >>> a.removeRoute('eth0', '192.168.5.0/24')
        >>> a.getListRoute()
        >>> a.removeRoute('eth0')
        >>> a.getListRoute()

        eth0:192.168.5.14/24 successful added
        Route to 192.168.22.0/24 via 192.168.5.20 successful added
        Routes:
        target: 127.0.0.0/8 source: 127.0.0.1 dev: lo
        target: 192.168.5.0/24 source: 192.168.5.1 dev: eth0
        target: 192.168.22.0/24 source: 192.168.5.20 dev: eth0
        192.168.5.0/24 deleted from eth0
        Routes:
        target: 127.0.0.0/8 source: 127.0.0.1 dev: lo
        target: 192.168.22.0/24 source: 192.168.5.20 dev: eth0
        routes from eth0 deleted
        Routes:
        target: 127.0.0.0/8 source: 127.0.0.1 dev: lo
        """
        if rem_network is not None:
            if rem_interface in self.routes.keys():
                if ipa.IPv4Interface(rem_network).network in self.routes[rem_interface].keys():
                    self.routes[rem_interface].pop(ipa.IPv4Interface(rem_network).network)
                    print(f"{rem_network} deleted from {rem_interface}")
        else:
            self.routes.pop(rem_interface)
            print(f"routes from {rem_interface} deleted")

    def getListRoute(self):
        """Выводит таблицу маршрутизации.

        Example:
        >>> a = Router()
        >>> a.addIP('eth0', '192.168.5.14/24')
        >>> a.addIP('eth1', '192.168.55.14/24')

        Routes:
        target: 127.0.0.0/8 source: 127.0.0.1 dev: lo
        target: 192.168.5.0/24 source: 192.168.5.1 dev: eth0
        target: 192.168.55.0/24 source: 192.168.55.1 dev: eth1
        """
        print(f"Routes:")
        for i in self.routes.keys():
            for j in self.routes[i]:
                print(f"target: {j} source: {self.routes[i][j]} dev: {i}")
