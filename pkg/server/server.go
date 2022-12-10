package server

import (
	"fmt"
	"log"
	"net"
	"flag"

	"google.golang.org/grpc"

	pb "github.com/sekuradev/apigolang/sekuraapi/v1"
)

var (
	port = flag.Int("port", 8080, "The server port")
)

type Server interface {
    Serve()
}

type server struct {
	agent pb.UnimplementedAgentServiceServer
	ui pb.UnimplementedUIServiceServer
}

func (s *server) Serve() {
	lis, err := net.Listen("tcp", fmt.Sprintf(":%d", *port))
	if err != nil {
		log.Fatalf("failed to listen: %v", err)
	}
	gs := grpc.NewServer()
	pb.RegisterAgentServiceServer(gs, s.agent)
	pb.RegisterUIServiceServer(gs, s.ui)
	log.Printf("server listening at %v", lis.Addr())
	if err := gs.Serve(lis); err != nil {
		log.Fatalf("failed to serve: %v", err)
	}
}

func NewServer() Server{
	return &server{
	}
}
