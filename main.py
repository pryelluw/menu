from models import Menu

def main():
    m = Menu()
    m.load_meals() # 2 meals a day for 7 days
    menu = m.generate()
    m.write(menu)


if __name__ == '__main__':
    main()
    print('Done!')
