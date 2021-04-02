# Logic Gate Implementation

class LogicGate(object):
	def __init__(self, lbl):
		self.label = lbl
		self.output = None

	def get_label(self):
		return self.label

	def get_output(self):
		self.output = self.perform_gate_logic()
		return self.output

class BinaryGate(LogicGate):
	def __init__(self, lbl):
		super().__init__(lbl)
		self.pin_a = None
		self.pin_b = None

	def get_pin_a(self):
		if self.pin_a == None:
			return int(input(f'Enter Pin a input for gate {self.get_label()} : '))
		else:
			return self.pin_a.get_from().get_output()

	def get_pin_b(self):
		if self.pin_b == None:
			return int(input(f'Enter Pin b input for gate {self.get_label()} : '))
		else:
			return self.pin_b.get_from().get_output()

	def set_next_pin(self, source):
		if self.pin_a == None:
			self.pin_a = source
		else:
			if self.pin_b == None:
				self.pin_b = source
			else:
				raise RuntimeError('Cannot Connect: NO EMPTY PINS on this gate')

class AndGate(BinaryGate):
	def __init__(self, lbl):
		super().__init__(lbl)

	def perform_gate_logic(self):
		a = self.get_pin_a()
		b = self.get_pin_b()

		return int(a == 1 and b == 1)

class OrGate(BinaryGate):
	def __init__(self, lbl):
		super().__init__(lbl)

	def perform_gate_logic(self):
		a = self.get_pin_a()
		b = self.get_pin_b()

		return int(a == 1 or b == 1)

class UnaryGate(LogicGate):
	def __init__(self, lbl):
		super().__init__(lbl)
		self.pin = None

	def get_pin(self):
		if self.pin == None:
			return int(input(f'Enter Pin input for gate {self.get_label()} : '))
		else:
			return self.pin.get_from().get_output()

	def set_next_pin(self, source):
		if self.pin == None:
			self.pin = source
		else:
			raise RuntimeError('Cannot Connect: NO EMPTY PINS on this gate')

class NotGate(UnaryGate):
	def __init__(self, lbl):
		super().__init__(lbl)

	def perform_gate_logic(self):
		return int(not self.get_pin())

class NandGate(AndGate):
	def perform_gate_logic(self):
		if self.perform_gate_logic() == 1:
			return 0
		return 1

class NorGate(OrGate):
	def perform_gate_logic(self):
		if self.perform_gate_logic() == 1:
			return 0
		return 1

class Connector:
	def __init__(self, fgate, tgate):
		self.from_gate = fgate
		self.to_gate = tgate
		tgate.set_next_pin(self)

	def get_from(self):
		return self.from_gate

	def get_to(self):
		return self.to_gate

if __name__ == '__main__':
	g1 = AndGate('G1')
	g2 = AndGate('G2')

	g3 = OrGate('G3')
	g4 = NotGate('G4')

	c1 = Connector(g1, g2)
	c2 = Connector(g2, g3)
	c3 = Connector(g3, g4)
	print(g4.get_output())