package main
import (
    "encoding/json"
    "net/http"
	"fmt"
)

type User struct {
	Id   int    `json:"id"`
	Name  string `json:"name"`
	Email string `json:"email"`
}

var users []User

func create_user(w http.ResponseWriter, r *http.Request) {    
    if r.Method != http.MethodPost {
        http.Error(w, "Method Not Allowed", http.StatusMethodNotAllowed)
        return
    }
    var user User
    json.NewDecoder(r.Body).Decode(&user)
    user.Id = 1
    users = append(users, user)
    w.Header().Set("Content-Type", "application/json")
    json.NewEncoder(w).Encode(user)
}
func main() {
    http.HandleFunc("/users", create_user)

    fmt.Println("Server running on http://localhost:8080")

    err := http.ListenAndServe(":8080", nil)
    fmt.Println("ListenAndServe returned:", err)
}
