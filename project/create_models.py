from models.base import Base


def create_models():
    Base.metadata.create_all()

if __name__ == '__main__':
    create_models()
