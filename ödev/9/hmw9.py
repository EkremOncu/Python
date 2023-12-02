# Solution 1

class CommandPrompt:
    def __init__(self,prompt):
        self.prompt = prompt

    def run(self):
        while True:
            prompt = input('write: ')
            print(prompt[::-1])

            if prompt == 'quit':
                return False

cp = CommandPrompt('CSD')
cp.run()
