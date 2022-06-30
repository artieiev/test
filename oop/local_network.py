class Data:
	def __init__(self, data, ip):
		self.data = data
		self.ip = ip


class Server:
	IP = 1

	def __init__(self):
		self.ip = Server.IP
		Server.IP += 1
		self.buffer = []
		self.router = None

	def send_data(self, data):
		self.router.buffer.append(data)
		

	def get_data(self):
		t = self.buffer
		self.buffer = []
		return t

	def get_ip(self):
		return self.ip


class Router:
	def __init__(self):
		self.buffer = []
		self.servers = {}

	def link(self, server):
		self.servers[server.get_ip()] = server
		server.router = self

	def unlink(self, server):
		del self.servers[server.get_ip()]
		server.router = None


	def send_data(self):
		for i in self.buffer:
			self.servers[i.ip].buffer.append(i)
		self.buffer = []


router = Router()
sv_from = Server()
router.link(sv_from)
router.link(Server())
router.link(Server())
sv_to = Server()
router.link(sv_to)
sv_from.send_data(Data("Hello", sv_to.get_ip()))
router.send_data()
sv_to.send_data(Data("Hi", sv_from.get_ip()))
router.send_data()
msg_lst_from = sv_from.get_data()
msg_lst_to = sv_to.get_data()
print(msg_lst_from)