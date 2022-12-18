package server

import (
	"flag"
)

var (
	port = flag.Int("port", 50051, "The server port")
)

type Server interface {
	Serve()
}
