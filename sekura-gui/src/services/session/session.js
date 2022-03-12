import axios from "axios";
import jwt_decode from 'jwt-decode';

export function login(user, password) {
  return axios.post("/api/token/", {
    username: user,
    password: password,
  },{
    headers: {
      "Content-Type": "application/json",
    },
  })
  .then((response) => {
    localStorage.setItem("access", response.data.access);
    localStorage.setItem("refresh", response.data.refresh);
    axios.defaults.headers.common['Authorization'] = "Authorization: Bearer " + response.data.access;
  })
}

export function isLogged() {
  try {
    var access = localStorage.getItem("access");
    var decoded = jwt_decode(access);
    if (Date.now() > decoded.exp * 1000) {
      return false;
    }
    return true;
  } catch (error){
    return false;
  }
}

export function logout() {
  localStorage.removeItem("access");
  localStorage.removeItem("refresh");
}

export function refresh(){
  var access = localStorage.getItem("access");
  var decoded = jwt_decode(access);
  console.log(localStorage.getItem("refresh"));
  console.log(access);
  console.log(decoded);

  return axios.post("/api/token/refresh/", {
    access: localStorage.getItem("access"),
    refresh: localStorage.getItem("refresh"),
  },{
    headers: {
      "Content-Type": "application/json",
    },
  })
  .then((response) => {
    if (response.data.access) {
      localStorage.setItem("access", response.data.access);
      axios.defaults.headers.common['Authorization'] = "Authorization: Bearer " + response.data.access;
    }
    if (response.data.refresh) {
      localStorage.setItem("refresh", response.data.refresh);
    }
  })
}
