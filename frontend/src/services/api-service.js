import client from "@/client";

class UserService {
  login(payload) {
    return client.post("auth/login/", payload);
  }

  register(payload) {
    return client.post("auth/register/", payload);
  }

  userDetail() {
    return client.get("user/detail/");
  }
}

export default new UserService();
