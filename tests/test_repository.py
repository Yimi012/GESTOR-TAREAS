import unittest
from repository import TaskRepository

class TestTaskRepository(unittest.TestCase):

    def setUp(self):
        # Se crea un repositorio limpio para cada prueba
        self.repo = TaskRepository()

    def test_add_task(self):
        task = self.repo.add_task("Estudiar para el examen")
        self.assertEqual(task.title, "Estudiar para el examen")
        self.assertFalse(task.completed)

    def test_complete_task(self):
        task = self.repo.add_task("Hacer ejercicio")
        completed_task = self.repo.complete_task(task.id)
        self.assertTrue(completed_task.completed)

    def test_delete_task(self):
        task = self.repo.add_task("Leer un libro")
        result = self.repo.delete_task(task.id)
        self.assertTrue(result)

if __name__ == "__main__":
    unittest.main()
