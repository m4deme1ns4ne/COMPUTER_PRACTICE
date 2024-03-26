package main

import (
	"fmt"
	"net/http"
)
 
func main() {
http.HandleFunc("/", func(w http.ResponseWriter, r *http.Request) {
fmt.Fprintf(w, "Волжанин Александр 05.03.2024 16:13")
})
http.ListenAndServe(":80", nil)
}