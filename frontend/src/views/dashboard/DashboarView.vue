<template>
  <BaseLayout>
     <div class="container py-5">
        <div class="row justify-content-center">
           <div class="col-md-8">
              <div class="card shadow">
                 <div class="card-header bg-dark text-white">
                    <p class="mb-0">Todo List</p>
                 </div>
                 <div class="card-body">
                    <div class="input-group mb-4">
                       <form @submit.prevent="addTodo" class="d-flex w-100">
                          <input
                             required
                             type="text"
                             v-model="memo"
                             class="form-control"
                             placeholder="Memo"
                             />
                          <button class="btn btn-primary ms-2" type="submit">
                          <i class="fas fa-plus me-1"></i> 
                          </button>
                       </form>
                    </div>
                    <div class="mt-3">
                       <TodoItem v-if="todos.length!=0" v-for="item in todos" :todoItem="item" :key="item.id" @item-deleted="removeTodoItem" @item-updated="updateTodoItem"></TodoItem>
                       <div v-else class="empty-state">
                          <i class="fas fa-clipboard-list fa-3x mb-3"></i>
                          <p>No tasks have been added yet.</p>
                       </div>
                    </div>
                 </div>
                 <div class="card-footer text-muted">
                    <div class="d-flex justify-content-between">
                       <span>{{ completedCount }} Task Complated</span>
                    </div>
                 </div>
              </div>
           </div>
        </div>
     </div>
  </BaseLayout>
</template>

<script>
  import BaseLayout from "@/layouts/BaseLayout.vue";
  import TodoItem from "@/components/TodoItem.vue"
  import TodoService from "@/services/todo-service.js";
  
  export default {
    components: {
      BaseLayout,
      TodoItem
    },
    data() {
      return {
        todos: [],
        memo: "",
        completedCount: 0,
      };
    },
    created() {
      this.fetchTodos();
    },
    computed: {
      completedCount() {
        return this.todos.filter(todo => todo.completed).length;
      }
    },
    methods: {
      async fetchTodos() {
        this.loading = true;
        try {
          const response = await TodoService.getAllTodos();
          this.todos = response.data;
        } catch (error) {
          console.error("Failed to fetch URLs:", error);
        } finally {
          this.loading = false;
        }
      },
      async addTodo(){
        this.loading = true;
        try {
          const response = await TodoService.createTodo({
            memo: this.memo
          });
          if (response?.status === 201) {
            this.todos.push(response.data);
            this.memo = "";
          } else {
            throw new Error('Invalid response format');
          }
        } catch (error) {
          console.error("Error:", error);
        }
        finally {
          this.loading = false;
        }
      },
  
      removeTodoItem(todoId) {
        this.todos = this.todos.filter(todo => todo.id !== todoId);
      },
  
      updateTodoItem(updatedTodo) {
        // Find and update the todo in the local array
        const index = this.todos.findIndex(todo => todo.id === updatedTodo.id);
        if (index !== -1) {
          // Replace the old todo with the updated one
          this.todos.splice(index, 1, updatedTodo);
        }
      },
    },
  };
</script>

<style scoped>
  .todo-item {
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 12px 15px;
  border-radius: 4px;
  margin-bottom: 8px;
  transition: all 0.3s;
  }
  .todo-item:hover {
  background-color: #f8f9fa;
  }
  .completed {
  text-decoration: line-through;
  color: #6c757d;
  }
  .empty-state {
  text-align: center;
  padding: 30px;
  color: #6c757d;
  }
</style>