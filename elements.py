from checks import Check


class Button(Check):
    def __init__(self, loc):
        self.loc = loc
        super(Button, self).__init__(self.loc)


class Input(Check):
    def __init__(self, loc):
        self.loc = loc
        super(Input, self).__init__(self.loc)


class Text(Check):
    def __init__(self, loc):
        self.loc = loc
        super(Text, self).__init__(self.loc)


class Picture(Check):
    def __init__(self, loc):
        self.loc = loc
        super(Picture, self).__init__(self.loc)
