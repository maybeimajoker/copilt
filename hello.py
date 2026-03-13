"""
一个简单的问候小程序 / A simple greeting program
"""


def greet(name: str) -> str:
    """Return a greeting message for the given name."""
    return f"你好，{name}！欢迎来到 copilt 🎉"


def farewell(name: str) -> str:
    """Return a farewell message for the given name."""
    return f"再见，{name}！祝你有美好的一天 👋"


if __name__ == "__main__":
    name = input("请输入你的名字 / Enter your name: ").strip() or "世界"
    print(greet(name))
    print(farewell(name))
