from langgraph.checkpoint.postgres import PostgresSaver
from backend.config.settings import POSTGRES_URL


class Database:
    def __init__(self):
        self.context = None
        self.checkpointer = None

    def initialize(self):
        if self.checkpointer is not None:
            return self.checkpointer

        if not POSTGRES_URL:
            raise ValueError("POSTGRES_URL not found in .env")

        try:
            self.context = PostgresSaver.from_conn_string(POSTGRES_URL)
            self.checkpointer = self.context.__enter__()
            self.checkpointer.setup()

            print("PostgreSQL checkpointer ready.")

            return self.checkpointer

        except Exception as e:
            self.checkpointer = None
            raise RuntimeError(f"PostgreSQL connection failed: {e}") from e

    def close(self):
        if self.context and self.checkpointer:
            try:
                self.context.__exit__(None,None,None)

            except Exception:
                pass

        self.checkpointer = None
        self.context = None