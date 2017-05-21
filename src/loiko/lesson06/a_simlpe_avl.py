task = '''
Оптимальное AVL-дерево поиска.
 
Заполните кодом все места, где вcтретится ключевое слово pass решая следующую задачу: 
 
Известны частоты появления ключевых слов в некоторой программе, то есть дана таблица вроде такой:
begin 5
do 40
else 8
end 4
if 10
then 10
while 23

Нужно построить двоичное AVL-дерево поиска: 
    - в вершинах стоят ключевые слова;
    - ключевое слово в каждой вершине лексикографически больше
    всех слов в левом поддереве и меньше всех слов в правом поддереве;

Вход - текстовый файл содержащий: 
    - список из n слов в алфавитном порядке; 
    - частоты их появления в тексте.
    Например:
        begin 5
        do 40
        else 8
        end 4
        if 10
        then 10
        while 23
Выход: 
    - двоичное AVL-дерево поиска. Дерево должно быть сбалансированным.
    Например:
            end
           /   \ 
         do     then
        /  \    /  \
    begin else if while
В этом задании не требуется предусматривать удаление узлов.
Поиск должен возвращать целый узел дерева (а не частоту или ключ).
Шаблон узла вам Node задан заранее. 
'''


# ----------------------------------- ДЕРЕВО ------------------------------------
class AvlA():
    # ------------------------------- ОТДЕЛЬНЫЙ УЗЕЛ ------------------------------------
    class Node():
        def __init__(self, key, value):
            self.key = key
            self.value = value
            self.left = None
            self.right = None
            self.height = 0

        def balance(self):
            return (self.left.height if self.left else -1) - (
                self.right.height if self.right else -1)

        def __str__(self):
            return str(self.key)

    def __init__(self, root=None):
        self.root = root  # корень
        self._outlist = list()  # вспомогательный лист в котором строится дерево для вывода его на экран

    def free(self):
        if not self.root:
            return
        self._free(self.root)

    def add(self, key, value):
        self.root = self._add(self.root, key, value)

    def lookup(self, key):
        return self._lookup(self.root, key)

    # заполните все методы (где есть pass) до состояния прохождения тестов
    def _free(self, tree):
        if tree:
            self._free(tree.left)
            self._free(tree.right)
            tree = None

    def _lookup(self, tree, key):
        while tree:
            if tree.key == key:
                return tree
            elif key < tree.key:
                tree = tree.left
            else:
                tree = tree.right
        return tree

    def _create(self, key, value):
        return self.Node(key, value)

    def _height(self, tree):
        return tree.height if tree else -1

    def _add(self, tree, key, value):
        pass
        if not tree:
            self.root = self._create(key, value)
            return self.root
        if (key < tree.key):
            tree.left = self._add(tree.left, key, value)
            if self._height(tree.left) - self._height(tree.right) == 2:
                if key < tree.left.key:
                    tree = self._right_rotate(tree)
                else:
                    tree = self._leftright_rotate(tree)
        elif (key > tree.key):
            tree.right = self._add(tree.right, key, value)
            if self._height(tree.right) - self._height(tree.left) == 2:
                if key > tree.right.key:
                    tree = self._left_rotate(tree)
                else:
                    tree = self._rightleft_rotate(tree)
        else:
            tree.value = value
        tree.height = max(self._height(tree.left), self._height(tree.right)) + 1
        return tree


    def _right_rotate(self, tree):
        root = tree.left
        tree.left = root.right
        root.right = tree
        tree.height = max(self._height(tree.left), self._height(tree.right)) + 1
        root.height = max(self._height(root.left), tree.height) + 1
        return root

    def _left_rotate(self, tree):
        root = tree.right
        tree.right = root.left
        root.left = tree
        tree.height = max(self._height(tree.left), self._height(tree.right)) + 1
        root.height = max(self._height(root.right), tree.height) + 1
        return root

    def _leftright_rotate(self, tree):
        tree.left = self._left_rotate(tree.left)
        return self._right_rotate(tree)

    def _rightleft_rotate(self, tree):
        tree.right = self._right_rotate(tree.right)
        return self._left_rotate(tree)


    # обновление массива для строкового представления дерева
    def _dfs_print(self, tree, level):
        if level == 0:
            self._outlist = list()
        if len(self._outlist) < level + 1:
            self._outlist.append(" ")
        self._outlist[level] += (str(tree) if tree else ".") + " "
        if tree:
            self._dfs_print(tree.left, level + 1)
            self._dfs_print(tree.right, level + 1)

    # строковое представление дерева
    def __str__(self) -> str:
        self._dfs_print(self.root, 0)
        out = ""
        max = 0
        for s_Level in self._outlist:
            if len(s_Level) > max:
                max = len(s_Level)
        for s_Level in self._outlist:
            spaces = ""
            line = s_Level
            while (len(line) <= max):
                line = s_Level
                spaces += " "
                line = line.replace(" ", spaces)
            subspaces = " " * (len(spaces) - 1)
            while (len(line) > max):
                line = line.replace(spaces, subspaces, 1)
            if len(line.replace(".", "").replace(" ", "")) > 0:
                out += line + "\n"
        out += "-" * max
        return out


# ------------------------ПРОВЕРКА РАБОТОСПОСОБНОСТИ -------------------------
def main():
    # чтение одной строки из файла
    def arr(filename):
        return filename.readline().replace("\n", "").split(" ")

    f = open("dataA.txt")
    count = int(arr(f)[0])
    avl = AvlA()
    for i in range(0, count):
        data = arr(f)
        assert len(data) == 2
        avl.add(data[0], int(data[1]))
    print(avl)


# Для ручной проверки нажмите Ctrl+Shift+F10
# установив курсор на  main
# или создайте конфигурацию Run-Edit configuration
if __name__ == "__main__":
    main()
