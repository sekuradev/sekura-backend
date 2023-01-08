package server

import (
	"context"
	"fmt"
	"log"
	"net"

	"google.golang.org/grpc"
	"google.golang.org/grpc/reflection"

	pb "github.com/sekuradev/apigolang/sekuraapi/v1"
)

type serverAgent struct {
	pb.UnimplementedAgentServiceServer
	options []grpc.ServerOption
}

func NewAgentServer(options []grpc.ServerOption) Server {
	return &serverAgent{options: options}
}

func (s *serverAgent) Serve() {
	lis, err := net.Listen("tcp", fmt.Sprintf("%s:%d", *serverName, *port))
	if err != nil {
		log.Fatalf("failed to listen: %v", err)
	}
	gs := grpc.NewServer(s.options...)
	pb.RegisterAgentServiceServer(gs, s)
	reflection.Register(gs)
	log.Printf("server listening at %v (%s:%d))", lis.Addr(), *serverName, *port)
	if err := gs.Serve(lis); err != nil {
		log.Fatalf("failed to serve: %v", err)
	}
}

func (s serverAgent) SetAccess(ctx context.Context, in *pb.SetAccessRequest) (*pb.SetAccessResponse, error) {
	fmt.Println("++")
	fmt.Printf("Items: %d\n", len(in.Accesses))
	fmt.Println("--")
	return &pb.SetAccessResponse{Error: false}, nil
}
