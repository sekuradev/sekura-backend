package main

import (
    "flag"

    "github.com/sekuradev/backend/pkg/server"
)

func main() {
    flag.Parse()
    server.NewServer().Serve()
}
