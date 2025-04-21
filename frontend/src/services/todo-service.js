import client from "../client";

class TodoService {
  getAllTodos() {
    return client.get("todos/");
  }

  createTodo(payload) {
    return client.post("todos/", payload);
  }

  getTodoDetail(id) {
    return client.get(`todos/${id}/`);
  }

  todoToogle(id) {
    return client.patch(`todos/${id}/toggle/`);
  }

  todoRemove(id) {
    return client.delete(`todos/${id}/`);
  }

  todoUpdate(id, payload) {
    return client.patch(`todos/${id}/`,payload);
  }
}

export default new TodoService();