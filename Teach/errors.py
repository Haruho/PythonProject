while True:
    try:
        x = int(input("请输入一个整数..."))
        break
    except ValueError:
        print("这不是一个整数，请重试...")
