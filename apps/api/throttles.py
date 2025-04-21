from rest_framework.throttling import UserRateThrottle

class UserTodoThrottle(UserRateThrottle):
    rate = '1000/day'
    scope = 'todo_'