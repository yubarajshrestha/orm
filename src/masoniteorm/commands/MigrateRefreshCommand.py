from cleo import Command
from ..migrations import Migration


class MigrateRefreshCommand(Command):
    """
    Rolls back all migrations and migrates them again.

    migrate:refresh
        {--c|connection=default : The connection you want to run migrations on}
        {--d|directory=databases/migrations : The location of the migration directory}
        {--s|seed=? : Seed database after refresh. The seeder to be ran can be provided in argument}
    """

    def handle(self):

        migration = Migration(
            command_class=self,
            connection=self.option("connection"),
            migration_directory=self.option("directory"),
        )

        migration.refresh()

        self.line("")

        if self.option("seed") == "null":
            self.call("seed:run", "None")
        elif self.option("seed"):
            self.call("seed:run", self.option("seed"))
