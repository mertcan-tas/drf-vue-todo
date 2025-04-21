<template>
    <div class="todo-item bg-light">
       <div class="d-flex align-items-center">
          <input
             type="checkbox"
             class="form-check-input me-2"
             v-model="todoItem.completed"
             @change="complateToggle"
             />
          <span :style="{ textDecoration: todoItem.completed ? 'line-through' : 'none' }">{{ todoItem.memo }}</span>
       </div>
       <div>
          <button @click="updateMemo" class="btn btn-sm btn-primary" style="margin-right: 8px;"><i class="fas fa-pen me-1"></i></button>
          <button @click="deleteUrl" class="btn btn-sm btn-danger"><i class="fas fa-trash me-1"></i></button>
       </div>
    </div>
 </template>

 <script>
    import TodoService from "@/services/todo-service.js";
    import Notiflix from 'notiflix';
    
    export default {
      props: {
        todoItem: Object,
      },
      methods: {
        async complateToggle() {
          try {
            const response = await TodoService.todoToogle(this.todoItem.id);
            if (response?.status === 200) {
              this.$emit('item-updated', {
                ...this.todoItem,
                completed: this.todoItem.completed
              });
            } else {
              throw new Error("Invalid response format");
            }
          } catch (error) {
            console.error("Todo could not be updated:", error);
            this.showNotification("Todo could not be updated", "error");
          }
        },
    
        updateMemo() {
          Notiflix.Confirm.prompt(
            "Update Todo",
            "Enter the new memo text:",
            this.todoItem.memo,
            "Update",
            "Cancel",
            async (newMemo) => {
              try {
                const response = await TodoService.todoUpdate(this.todoItem.id, { memo: newMemo });
                if (response?.status === 200) {
                  this.$emit('item-updated', {
                    ...this.todoItem,
                    memo: newMemo
                  });
                  this.showNotification("Todo updated successfully", "success");
                } else {
                  throw new Error('Invalid response format');
                }
              } catch (error) {
                console.error("Todo could not be updated:", error);
                this.showNotification("Todo could not be updated", "error");
              }
            },
            () => {
              this.showNotification("Update operation cancelled", "info");
            },
            {}
          );
        },
    
        deleteUrl() {
          Notiflix.Confirm.show(
            "Todo Delete Confirmation",
            "Are you sure you want to delete this todo?",
            "Yes",
            "No",
            async () => {
              try {
                const response = await TodoService.todoRemove(this.todoItem.id);
                if (response?.status === 204) {
                  this.$emit('item-deleted', this.todoItem.id);
                  this.showNotification("Delete successfully", "success");
                } else {
                  throw new Error('Invalid response format');
                }
              } catch (error) {
                console.error("URL could not be deleted:", error);
                this.showNotification("URL could not be deleted", "error");
              }
            },
            () => {
              this.showNotification("Delete operation cancelled", "info");
            },
            {}
          );
        },
        
        showNotification(message, type = "success") {
          if (type === "success") {
            Notiflix.Notify.success(message);
          } else if (type === "error") {
            Notiflix.Notify.failure(message);
          } else if (type === "info"){
            Notiflix.Notify.info(message);
          }
        }
      },
    };
 </script>