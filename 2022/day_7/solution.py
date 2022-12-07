def get_usable_input():
    with open('input.txt') as f:
        lines = f.readlines()

    inputs = []
    for line in lines:
        line = line.strip().split()
        inputs.append(line)
    return inputs


class Directory:
    def __init__(self, name, parent=None):
        self.name = name
        self.parent = parent
        self.children = []
        self.size = 0

    def get_directory(self, name):
        for child in self.children:
            if name == child.name:
                return child
        return None


class SpaceDeletion:

    def __init__(self):
        self.root = None
        self.current_directory = None

    def __contruct_directory_tree(self, inputs):
        for i, input in enumerate(inputs):
            if input[0] == '$':  # inputs starting with '$'
                if input[1] == 'cd':  # inputs starting with '$ cd'
                    if input[2] == '/':  # inputs starting with '$ cd /'
                        if not self.root:
                            self.root = Directory('/', None)
                        self.current_directory = self.root
                    elif input[2] == '..':  # inputs starting with '$ cd ..'
                        self.current_directory = self.current_directory.parent
                    else:  # inputs starting with '$ cd directory_name'
                        child_directory = self.current_directory.get_directory(input[2])
                        self.current_directory = child_directory
                elif input[1] == 'ls':  # inputs starting with '$ ls'
                    pass
            else:  # output of ls
                if input[0] == 'dir':  # outputs for directory
                    directory = Directory(input[1], parent=self.current_directory)
                    self.current_directory.children.append(directory)
                else:  # outputs for files
                    self.current_directory.size += int(input[0])

    def __accumulate_directory_sizes(self):

        def dfs(node):
            for child in node.children:
                node.size += dfs(child)
            return node.size

        dfs(self.root)

    def __get_directory_sizes(self, threshold=None):
        result = []

        def dfs(node):

            if threshold:
                if node.size <= threshold:
                    result.append(node.size)
            else:
                result.append(node.size)

            for child in node.children:
                dfs(child)

        dfs(self.root)
        return sorted(result)

    def no_space_left_part_1(self):
        inputs = get_usable_input()
        self.__contruct_directory_tree(inputs)
        self.__accumulate_directory_sizes()

        threshold = 100000

        small_directory_sizes = self.__get_directory_sizes(threshold)
        return sum(small_directory_sizes)

    def no_space_left_part_2(self):
        inputs = get_usable_input()
        self.__contruct_directory_tree(inputs)
        self.__accumulate_directory_sizes()

        file_system_size = 70000000
        unused_threshold = 30000000

        current_unused = file_system_size - self.root.size
        directory_sizes = self.__get_directory_sizes()

        for i in range(len(directory_sizes)):
            if current_unused + directory_sizes[i] >= unused_threshold:
                return directory_sizes[i]


print(SpaceDeletion().no_space_left_part_1())
print(SpaceDeletion().no_space_left_part_2())
