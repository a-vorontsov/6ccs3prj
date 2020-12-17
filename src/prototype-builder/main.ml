open Printf
open Instruction
open Bytecode

let emit b = String.concat "\n" (List.map as_string b)

let parse s =
  let lexbuf = Lexing.from_string s in
  let ast = Parser.prog Lexer.token lexbuf in
  ast

let parse_file f =
  let input = open_in f in
  let filebuf = Lexing.from_channel input in
  try
    Ok
      (emit
         (gen_bytecode
            (Parse.parse filebuf (Parser.Incremental.prog filebuf.lex_curr_p))))
  with
  | Lexer.Error msg -> Error (sprintf "%s!" msg)
  | Parser.Error ->
      Error
        (sprintf "Syntax error at offset %d:\n%!" (Lexing.lexeme_start filebuf))
  | Util.Syntax_error (location, msg) -> (
      match location with
      | Some (line, pos) ->
          Error (sprintf "Syntax error at %d:%d\n%s" line pos msg)
      | None -> Error (sprintf "%s" msg) )

let write_file s out =
  let oc = open_out_bin (out ^ ".avb") in
  let b = Bytes.of_string s in
  output_bytes oc b;
  close_out oc

let () =
  if Array.length Sys.argv == 2 then (
    let file = Sys.argv.(1) in
    ignore print_newline;
    let bc = parse_file file in
    match bc with
    | Ok x -> write_file x (Filename.remove_extension file)
    | Error e ->
        eprintf "%s" e;
        exit (-1) )