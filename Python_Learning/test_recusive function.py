def func_generating_exception():
    try:
        raise Exception("He created me")
    except Exception as e:
        try:
            raise Exception("Hahah")
        except Exception as e:
            print("Cannot Handle this")

        # func_generating_exception()



if __name__ == "__main__":
    func_generating_exception()
