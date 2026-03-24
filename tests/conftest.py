#import os
#os.environ["DATABASE_URL"] = "sqlite://"

import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from app.main import app
from app.db import Base, get_db
from app.models import todo_model
from sqlalchemy.pool import StaticPool

TEST_DATABASE_URL = "sqlite://"

engine = create_engine(
    TEST_DATABASE_URL,
    connect_args={"check_same_thread": False},
    poolclass=StaticPool
)

#TEST_DATABASE_URL = "sqlite:///./test.db"

#engine = create_engine(
#    TEST_DATABASE_URL,
#    connect_args={"check_same_thread": False}
#)

TestingSessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

@pytest.fixture(scope="session")
def test_db():
    
    print("ENGINE:", engine.url)
    Base.metadata.create_all(bind=engine)

    yield

    Base.metadata.drop_all(bind=engine)

@pytest.fixture(scope="function")
def db_session(test_db):

    connection = engine.connect()

    transaction = connection.begin()

    session = TestingSessionLocal(bind=connection)

    print("TEST DB:", engine.url)

    yield session

    session.close()

    transaction.rollback()

    connection.close()

@pytest.fixture(scope="function")
def client(db_session):

    def override_get_db():
        yield db_session

    app.dependency_overrides[get_db] = override_get_db

    return TestClient(app)

