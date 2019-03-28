from colorama import init, Fore, Back
init(autoreset=False)
class Color(object):
    #  前景色:红色  背景色:默认
    @classmethod
    def red(self, s):
        return Fore.RED + s + Fore.RESET

    @classmethod
    #  前景色:绿色  背景色:默认
    def green(self, s):
        return Fore.GREEN + s + Fore.RESET

    @classmethod
    #  前景色:黄色  背景色:默认
    def yellow(self, s):
        return Fore.YELLOW + s + Fore.RESET

    #  前景色:蓝色  背景色:默认
    @classmethod
    def blue(self, s):
        return Fore.BLUE + s + Fore.RESET

    #  前景色:洋红色  背景色:默认
    @classmethod
    def magenta(self, s):
        return Fore.MAGENTA + s + Fore.RESET

    #  前景色:青色  背景色:默认
    @classmethod
    def cyan(self, s):
        return Fore.CYAN + s + Fore.RESET

    #  前景色:白色  背景色:默认
    @classmethod
    def white(self, s):
        return Fore.WHITE + s + Fore.RESET

    #  前景色:黑色  背景色:默认
    @classmethod
    def black(self, s):
        return Fore.BLACK

    #  前景色:白色  背景色:绿色
    @classmethod
    def white_green(self, s):
        return Fore.WHITE + Back.GREEN + s + Fore.RESET + Back.RESET