module top_file#(
    parameter WIDTH = 32,
    parameter DEPTH = 2048
)(
    input wire [WIDTH-1:0] data_in,
    input wire clk,
    input wire write,
    input wire read,
    output wire [WIDTH-1:0] data_out,
    output wire fifo_full,
    output wire fifo_empty,
    output wire fifo_not_empty,
    output wire fifo_not_full
);


fifo  #(.DEPTH(DEPTH), .WIDTH(WIDTH))
	u0 (
	data_in,
	clk,
	write,
	read,
	data_out,
	fifo_full,
	fifo_empty,
	fifo_not_empty,
	fifo_not_full
	);



endmodule
