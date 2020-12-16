/*
   !!! KEINE ÄNDERUNGEN IN DIESER DATEI !!!
*/

#pragma once

// ####################################
// includes

#include <stdint.h>

// ####################################
// typedefs

typedef uint8_t u8;   // 8-bit unsigned integer
typedef uint16_t u16; // 16-bit unsigned integer
typedef uint32_t u32; // 32-bit unsigned integer

typedef int8_t i8;   // 8-bit signed integer
typedef int16_t i16; // 16-bit signed integer
typedef int32_t i32; // 32-bit signed integer

// ####################################
// functions

// Debug Output
void print_state(u8 state[4][4]);
void print_roundkey(u8 roundkey[3][4][4]);

// SubCells
void sub_cells(u8 state[4][4]);
void sub_cells_inv(u8 state[4][4]);

// AddConstants
void add_constants(u8 state[4][4], const u8 round);

// AddRoundkey
void add_roundkey(u8 state[4][4], u8 key[3][4][4]);
void add_roundkey_inv(u8 state[4][4], u8 key[3][4][4]);

// ShiftRows
void shift_rows(u8 state[4][4]);
void shift_rows_inv(u8 state[4][4]);

// MixColumns
void mix_columns(u8 state[4][4]);
void mix_columns_inv(u8 state[4][4]);

// Encrypt/Decrypt
void encrypt(const u8 plaintext[16], const u8 key[48], u8 ciphertext[16]);
void decrypt(const u8 ciphertext[16], const u8 key[48], u8 plaintext[16]);
