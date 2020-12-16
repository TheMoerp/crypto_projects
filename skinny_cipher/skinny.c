/*
 *   Einführung in die Kryptographie 1
 *   Projekt: SKINNY-128-384
 *
 *   Gruppe         : CB
 * 
 *   Name           : Julius Tim Gerecke
 *   Matrikelnummer : 108019210685
 * 
 *   Name           : Matthias Hottgenroth
 *   Matrikelnummer : 108019206675
 */

// ####################################
// includes

#include "skinny.h"
#include <stdio.h>

// ####################################
// static variables

// S-Box
static const u8 s_box[] = {0x65, 0x4c, 0x6a, 0x42, 0x4b, 0x63, 0x43, 0x6b, 0x55, 0x75, 0x5a, 0x7a, 0x53, 0x73, 0x5b, 0x7b, 0x35, 0x8c, 0x3a, 0x81, 0x89, 0x33, 0x80, 0x3b, 0x95, 0x25, 0x98, 0x2a, 0x90, 0x23, 0x99, 0x2b, 0xe5, 0xcc, 0xe8, 0xc1, 0xc9, 0xe0, 0xc0, 0xe9, 0xd5, 0xf5, 0xd8, 0xf8, 0xd0, 0xf0, 0xd9, 0xf9, 0xa5, 0x1c, 0xa8, 0x12, 0x1b, 0xa0, 0x13, 0xa9, 0x05, 0xb5, 0x0a, 0xb8, 0x03, 0xb0, 0x0b, 0xb9, 0x32, 0x88, 0x3c, 0x85, 0x8d, 0x34, 0x84, 0x3d, 0x91, 0x22, 0x9c, 0x2c, 0x94, 0x24, 0x9d, 0x2d, 0x62, 0x4a, 0x6c, 0x45, 0x4d, 0x64, 0x44, 0x6d, 0x52, 0x72, 0x5c, 0x7c, 0x54, 0x74, 0x5d, 0x7d, 0xa1, 0x1a, 0xac, 0x15, 0x1d, 0xa4, 0x14, 0xad, 0x02, 0xb1, 0x0c, 0xbc, 0x04, 0xb4, 0x0d, 0xbd, 0xe1, 0xc8, 0xec, 0xc5, 0xcd, 0xe4, 0xc4, 0xed, 0xd1, 0xf1, 0xdc, 0xfc, 0xd4, 0xf4, 0xdd, 0xfd, 0x36, 0x8e, 0x38, 0x82, 0x8b, 0x30, 0x83, 0x39, 0x96, 0x26, 0x9a, 0x28, 0x93, 0x20, 0x9b, 0x29, 0x66, 0x4e, 0x68, 0x41, 0x49, 0x60, 0x40, 0x69, 0x56, 0x76, 0x58, 0x78, 0x50, 0x70, 0x59, 0x79, 0xa6, 0x1e, 0xaa, 0x11, 0x19, 0xa3, 0x10, 0xab, 0x06, 0xb6, 0x08, 0xba, 0x00, 0xb3, 0x09, 0xbb, 0xe6, 0xce, 0xea, 0xc2, 0xcb, 0xe3, 0xc3, 0xeb, 0xd6, 0xf6, 0xda, 0xfa, 0xd3, 0xf3, 0xdb, 0xfb, 0x31, 0x8a, 0x3e, 0x86, 0x8f, 0x37, 0x87, 0x3f, 0x92, 0x21, 0x9e, 0x2e, 0x97, 0x27, 0x9f, 0x2f, 0x61, 0x48, 0x6e, 0x46, 0x4f, 0x67, 0x47, 0x6f, 0x51, 0x71, 0x5e, 0x7e, 0x57, 0x77, 0x5f, 0x7f, 0xa2, 0x18, 0xae, 0x16, 0x1f, 0xa7, 0x17, 0xaf, 0x01, 0xb2, 0x0e, 0xbe, 0x07, 0xb7, 0x0f, 0xbf, 0xe2, 0xca, 0xee, 0xc6, 0xcf, 0xe7, 0xc7, 0xef, 0xd2, 0xf2, 0xde, 0xfe, 0xd7, 0xf7, 0xdf, 0xff};

// invertierte S-Box
static const u8 s_box_inv[] = {0xac, 0xe8, 0x68, 0x3c, 0x6c, 0x38, 0xa8, 0xec, 0xaa, 0xae, 0x3a, 0x3e, 0x6a, 0x6e, 0xea, 0xee, 0xa6, 0xa3, 0x33, 0x36, 0x66, 0x63, 0xe3, 0xe6, 0xe1, 0xa4, 0x61, 0x34, 0x31, 0x64, 0xa1, 0xe4, 0x8d, 0xc9, 0x49, 0x1d, 0x4d, 0x19, 0x89, 0xcd, 0x8b, 0x8f, 0x1b, 0x1f, 0x4b, 0x4f, 0xcb, 0xcf, 0x85, 0xc0, 0x40, 0x15, 0x45, 0x10, 0x80, 0xc5, 0x82, 0x87, 0x12, 0x17, 0x42, 0x47, 0xc2, 0xc7, 0x96, 0x93, 0x03, 0x06, 0x56, 0x53, 0xd3, 0xd6, 0xd1, 0x94, 0x51, 0x04, 0x01, 0x54, 0x91, 0xd4, 0x9c, 0xd8, 0x58, 0x0c, 0x5c, 0x08, 0x98, 0xdc, 0x9a, 0x9e, 0x0a, 0x0e, 0x5a, 0x5e, 0xda, 0xde, 0x95, 0xd0, 0x50, 0x05, 0x55, 0x00, 0x90, 0xd5, 0x92, 0x97, 0x02, 0x07, 0x52, 0x57, 0xd2, 0xd7, 0x9d, 0xd9, 0x59, 0x0d, 0x5d, 0x09, 0x99, 0xdd, 0x9b, 0x9f, 0x0b, 0x0f, 0x5b, 0x5f, 0xdb, 0xdf, 0x16, 0x13, 0x83, 0x86, 0x46, 0x43, 0xc3, 0xc6, 0x41, 0x14, 0xc1, 0x84, 0x11, 0x44, 0x81, 0xc4, 0x1c, 0x48, 0xc8, 0x8c, 0x4c, 0x18, 0x88, 0xcc, 0x1a, 0x1e, 0x8a, 0x8e, 0x4a, 0x4e, 0xca, 0xce, 0x35, 0x60, 0xe0, 0xa5, 0x65, 0x30, 0xa0, 0xe5, 0x32, 0x37, 0xa2, 0xa7, 0x62, 0x67, 0xe2, 0xe7, 0x3d, 0x69, 0xe9, 0xad, 0x6d, 0x39, 0xa9, 0xed, 0x3b, 0x3f, 0xab, 0xaf, 0x6b, 0x6f, 0xeb, 0xef, 0x26, 0x23, 0xb3, 0xb6, 0x76, 0x73, 0xf3, 0xf6, 0x71, 0x24, 0xf1, 0xb4, 0x21, 0x74, 0xb1, 0xf4, 0x2c, 0x78, 0xf8, 0xbc, 0x7c, 0x28, 0xb8, 0xfc, 0x2a, 0x2e, 0xba, 0xbe, 0x7a, 0x7e, 0xfa, 0xfe, 0x25, 0x70, 0xf0, 0xb5, 0x75, 0x20, 0xb0, 0xf5, 0x22, 0x27, 0xb2, 0xb7, 0x72, 0x77, 0xf2, 0xf7, 0x2d, 0x79, 0xf9, 0xbd, 0x7d, 0x29, 0xb9, 0xfd, 0x2b, 0x2f, 0xbb, 0xbf, 0x7b, 0x7f, 0xfb, 0xff};

// vorberechnete Rundenkonstanten
static const u8 round_const[] = {0x01, 0x03, 0x07, 0x0F, 0x1F, 0x3E, 0x3D, 0x3B, 0x37, 0x2F, 0x1E, 0x3C, 0x39, 0x33, 0x27, 0x0E, 0x1D, 0x3A, 0x35, 0x2B, 0x16, 0x2C, 0x18, 0x30, 0x21, 0x02, 0x05, 0x0B, 0x17, 0x2E, 0x1C, 0x38, 0x31, 0x23, 0x06, 0x0D, 0x1B, 0x36, 0x2D, 0x1A, 0x34, 0x29, 0x12, 0x24, 0x08, 0x11, 0x22, 0x04, 0x09, 0x13, 0x26, 0x0c, 0x19, 0x32, 0x25, 0x0a, 0x15, 0x2a, 0x14, 0x28, 0x10, 0x20};

// Permutation P_T des Schlüsselfahrplans
static const u8 key_perm[] = {9, 15, 8, 13, 10, 14, 12, 11, 0, 1, 2, 3, 4, 5, 6, 7};

// inverse Permutation P_T^{-1} des Schlüsselfahrplans
static const u8 key_perm_inv[] = {8, 9, 10, 11, 12, 13, 14, 15, 2, 0, 4, 7, 6, 3, 5, 1};

// Parameter der 4x4 Matrix
#define MATRIX_SIZE 4

// es gibt 3 Schlüsselteile
#define NUMBER_OF_KEYPARTS 3

// Anzahl Zeilen der Schlüsselmatrix die bei addRoundKey verwendet werden und auf die LFSRs angewendet werden
#define USED_KEY_ROWS 2

// Byte Länge eines Schlüsselteils
#define NUM_OF_BYTES 16

// Rundenanzahl
#define NUM_OF_ROUNDS 56


// ####################################
// Debug Funktionen
// !!! KEINE ÄNDERUNGEN AN DIESEN FUNKTIONEN !!!

void print_state(u8 state[4][4])
{
    i32 i, j;

    printf("{");
    for (i = 0; i < 4; i++)
    {
        printf("{");
        for (j = 0; j < 4; j++)
        {
            printf("0x%02x", state[i][j]);
            if (j < 3)
            {
                printf(", ");
            }
            else
            {
                if (i < 3)
                {
                    printf("}, ");
                }
                else
                {
                    printf("}");
                }
            }
        }
    }
    printf("}");
}

void print_roundkey(u8 roundkey[3][4][4])
{
    printf("{");
    print_state(roundkey[0]);
    printf(", ");
    print_state(roundkey[1]);
    printf(", ");
    print_state(roundkey[2]);
    printf("}");
}

// ####################################
// SKINNY-128-384 Funktionen

void sub_cells(u8 state[4][4])
{
    // TODO: SubBytes Operation: Für jedes Byte des Zustands die S-Box aufrufen und Ergebnis zurück in den Zustand schreiben
    for(u8 i = 0; i < MATRIX_SIZE; i++) {
        for(u8 j = 0; j < MATRIX_SIZE; j++) {
            state[i][j] = s_box[state[i][j]];
        }
    }

}

void sub_cells_inv(u8 state[4][4])
{
    // TODO: Inverse SubBytes Operation: Für jedes Byte des Zustands die inverse S-Box aufrufen und Ergebnis zurück in den Zustand schreiben
    for(u8 i = 0; i < MATRIX_SIZE; i++) {
        for(u8 j = 0; j < MATRIX_SIZE; j++) {
            state[i][j] = s_box_inv[state[i][j]];
        }
    }
}

void add_constants(u8 state[4][4], const u8 round)
{
    /*
     *  TODO: AddConstants Operation: Rundenkonstante aufteilen, auf die passenden Bytes des Zustands addieren und Ergebnis zurück in den Zustand schreiben.
     *  Entsprechend der Vorlage zu addConstants (s.4) werden die Bits rc3 .. rc0 ausmaskiert und mit der 
     *  Position (0,0) der state Matrix ver-XOR-t.
     *  Anschließend werden die Bits rc5 .. rc4 ausmaskiert und auf die niederwertigsten Positionen geschoben
     *  und mit der Position (1,0) der state Matrix ver-XOR-t.
     *  Entsprechend der Vorlage die Position (2,0) der state Matrix mit der Konstanten 2 ver-XOR-t.
     */
    state[0][0] ^= round_const[round] & 0x0f;         // c0: 0x0f = 0b1111   leider werden Binär-Literale bei den vom Makefile vorgegebenen Compiler-Einstellungen
    state[1][0] ^= (round_const[round] & 0x30) >> 4;  // c1: 0x30 = 0b110000 nicht unterstützt, deshalb hier Hex-Darstellung
    state[2][0] ^= 0x02;  // c2
}

void add_roundkey(u8 state[4][4], u8 key[3][4][4])
{
    /*
     * TODO: AddRoundkey Operation: Rundenschlüssel auf Zustand anwenden, Rundenschlüssel aktualisieren und Ergebnis zurück in den Zustand bzw. den Schlüssel schreiben
     * Es werden entsprechend der Vorlage die Konstanten Bit-Positionen deklariert, welche in den LFSRs rückgekoppelt werden.
     * Die for-Schleife führt die addRoundKey-Operationen für jeden Teilschlüssel durch.
     */
    const u8 K1_LFSR_BITPOS1 = 7;
    const u8 K1_LFSR_BITPOS2 = 5;

    const u8 K2_LFSR_BITPOS1 = 6;
    const u8 K2_LFSR_BITPOS2 = 0;

    for(u8 i = 0; i < NUMBER_OF_KEYPARTS; i++) {
        u8 tmpKey[MATRIX_SIZE][MATRIX_SIZE];

    // 1. Rundenschlüssel auf aktuellen Zustand anwenden und Ergebnis zurück in den Zustand schreiben
        for(u8 j = 0; j < USED_KEY_ROWS; j++) {
            for(u8 k = 0; k < MATRIX_SIZE; k++) {
                state[j][k] ^= key[i][j][k];
            }
        }

    /* 
     * 2. Schlüsselpermutation P_T auf aktuellen Schlüssel anwenden und Ergebnis in temporärem Schlüsselarray abspeichern
     * In der for-Schleife wird zunächst die Index-Variable j so umgerechnet, 
     * dass die aktuelle Zeile und Spalte der 4x4 Matrix abgebildet wird.
     * Der aktuelle Inhalt des key_perm Arrays wird ebenfalls entsprechend umgerechnet.
     * Schließlich wird an die aktuelle Position, in dem temporären Schlüsselarray, das Byte an der
     * permutierten Position des ursprünglichen Schlüsselarry gesetzt.
     * Dieser Vorgang wiederholt sich für alle 16 Bytes eines Teilschlüssels.
     */
        for(u8 j = 0; j < NUM_OF_BYTES; j++) {
            u8 curNewRow = j / MATRIX_SIZE;
            u8 curNewColumn = j % MATRIX_SIZE;
            u8 curRow = key_perm[j] / MATRIX_SIZE;
            u8 curColumn = key_perm[j] % MATRIX_SIZE;
            tmpKey[curNewRow][curNewColumn] = key[i][curRow][curColumn];
        }

    /* 
     * 3. Ergebnis der Permutation mit LFSRs aktualisieren und wieder in temporären Speicher schreiben
     * Zunächst wird geprüft ob es sich bei dem aktuellen Teilschlüssel um K2 oder K3 handelt. Ist dies nicht
     * der Fall, so ist kein LFSR nötig. Anschließend durchlaufen die beiden darauffolgenden for-Schleifen
     * die ersten beiden Zeilen und alle vier Spalten. Innerhalb dieser for-Schleifen wird überprüft,
     * um welchen der beiden Teilschlüssel es sich handelt. Daraufhin wird das entsprechende LFSR auf jeden Byte
     * des tmpKey-Arrays angewendet (bis auf die unteren zwei Spalten).
     */ 
        if(i != 0) {
            for(u8 j = 0; j < USED_KEY_ROWS; j++) {
                for(u8 k = 0; k < MATRIX_SIZE; k++) {
                    if(i == 1) {
                        /*
                         * LFSR zu K2:
                         * Zu Beginn werden die Bytes um 7 und 5 Bit Positionen nach links verschoben und
                         * anschließend mit 0x01 ver-UND-et.
                         */
                        u8 bit1 = (tmpKey[j][k] >> K1_LFSR_BITPOS1) & 0x01; 
                        u8 bit2 = (tmpKey[j][k] >> K1_LFSR_BITPOS2) & 0x01;

                        tmpKey[j][k] = ((tmpKey[j][k] << 1) ^ bit1 ^ bit2);
                    } else {
                        /*
                         * LFSR zu K3:
                         * Zu Beginn werden die Byte auf die höchstwertigste Position
                         * geschoben also um "7 - die jeweiligen Bit Positionen". Anschließend wird mit
                         * 0x80 (0b10000000) ver-UND-et.
                         */
                        u8 bit1 = (tmpKey[j][k] << (7 - K2_LFSR_BITPOS1)) & 0x80;
                        u8 bit2 = (tmpKey[j][k] << (7 - K2_LFSR_BITPOS2)) & 0x80;

                        tmpKey[j][k] = (tmpKey[j][k] >> 1) ^ bit1 ^ bit2;
                    }
                }
            }
        }
    
    // 4. Temporären Speicher in Schlüssel zurückschreiben
        for(u8 j = 0; j < MATRIX_SIZE; j++) {
            for(u8 k = 0; k < MATRIX_SIZE; k++) {
                key[i][j][k] = tmpKey[j][k];
            }
        }

    }

}

void add_roundkey_inv(u8 state[4][4], u8 key[3][4][4])
{
    /*
     * TODO: Inverse AddRoundkey Operation: Rundenschlüssel rückwärts aktualisieren, Rundenschlüssel auf Zustand anwenden und Ergebnis zurück in den Zustand bzw. den Schlüssel schreiben
     * Es werden die Konstanten Bit-Positionen deklariert, welche in den Inversen LFSRs rückgekoppelt werden.
     * Die for-Schleife führt die Inverse addRoundKey-Operationen für jeden Teilschlüssel durch.
     */
    const u8 K1_LFSR_BITPOS1 = 6;
    const u8 K1_LFSR_BITPOS2 = 0;

    const u8 K2_LFSR_BITPOS1 = 7;
    const u8 K2_LFSR_BITPOS2 = 5;

    for(u8 i = 0; i < NUMBER_OF_KEYPARTS; i++) {
        u8 tmpKey[MATRIX_SIZE][MATRIX_SIZE];

    /*
     * 1. Inverse Schlüsselpermutation P_T^{-1} auf aktuellen Schlüssel anwenden und Ergebnis in temporärem Schlüsselarray abspeichern
     * In der for-Schleife wird zunächst die Index-Variable j so umgerechnet, 
     * dass die aktuelle Zeile und Spalte der 4x4 Matrix abgebildet wird.
     * Der aktuelle Inhalt des key_perm_inv Arrays wird ebenfalls entsprechend umgerechnet.
     * Schließlich wird an die aktuelle Position, in dem temporären Schlüsselarray, das Byte an der
     * permutierten Position des ursprünglichen Schlüsselarry gesetzt.
     * Dieser Vorgang wiederholt sich für alle 16 Bytes eines Teilschlüssels.
     */
        for(u8 j = 0; j < NUM_OF_BYTES; j++) {
            u8 curNewRow = j / MATRIX_SIZE;
            u8 curNewColumn = j % MATRIX_SIZE;
            u8 curRow = key_perm_inv[j] / MATRIX_SIZE;
            u8 curColumn = key_perm_inv[j] % MATRIX_SIZE;
            tmpKey[curNewRow][curNewColumn] = key[i][curRow][curColumn];
        }

        

    /* 
     * 2. Ergebnis der Permutation mit komplementärem LFSRs aktualisieren und wieder in temporären Speicher schreiben
     * Zunächst wird geprüft ob es sich bei dem aktuellen Teilschlüssel um K2 oder K3 handelt. Ist dies nicht
     * der Fall, so ist kein LFSR nötig. Anschließend durchlaufen die beiden darauffolgenden for-Schleifen
     * die letzen beiden Zeilen und alle vier Spalten. Innerhalb dieser for-Schleifen wird überprüft,
     * um welchen der beiden Teilschlüssel es sich handelt. Daraufhin wird das entsprechende LFSR auf jeden Byte
     * des tmpKey-Arrays angewendet (bis auf die oberen zwei Spalten).
     */ 
        if(i != 0) {
            for(u8 j = USED_KEY_ROWS; j < MATRIX_SIZE; j++) {
                for(u8 k = 0; k < MATRIX_SIZE; k++) {
                    if(i == 1) {
                        /*
                         * LFSR zu K2:
                         * Zu Beginn werden die Byte auf die höchstwertigste Position
                         * geschoben also um "7 - die jeweiligen Bit Positionen". Anschließend wird mit
                         * 0x80 (0b10000000) ver-UND-et.
                         */
                        u8 bit1 = (tmpKey[j][k] << (7 - K1_LFSR_BITPOS1)) & 0x80;
                        u8 bit2 = (tmpKey[j][k] << (7 - K1_LFSR_BITPOS2)) & 0x80;

                        tmpKey[j][k] = (tmpKey[j][k] >> 1) ^ bit1 ^ bit2;
                    } else {
                        /*
                         * LFSR zu K3:
                         * Zu Beginn werden die Bytes um 7 und 5 Bit Positionen nach links verschoben und
                         * anschließend mit 0x01 ver-UND-et.
                         */
                        u8 bit1 = (tmpKey[j][k] >> K2_LFSR_BITPOS1) & 0x01; 
                        u8 bit2 = (tmpKey[j][k] >> K2_LFSR_BITPOS2) & 0x01;

                        tmpKey[j][k] = ((tmpKey[j][k] << 1) ^ bit1 ^ bit2);
                    }
                }
            }
        }

    // 3. Temporären Speicher in Schlüssel zurückschreiben
        for(u8 j = 0; j < MATRIX_SIZE; j++) {
            for(u8 k = 0; k < MATRIX_SIZE; k++) {
                key[i][j][k] = tmpKey[j][k];
            }
        }

    
    // 4. Rundenschlüssel auf aktuellen Zustand anwenden und Ergebnis zurück in den Zustand schreiben
        for(u8 j = 0; j < USED_KEY_ROWS; j++) {
            for(u8 k = 0; k < MATRIX_SIZE; k++) {
                state[j][k] ^= key[i][j][k];
            }
        }
    
    }

}

void shift_rows(u8 state[4][4])
{
    /* TODO: ShiftRows Operation: Schiebe zweite Zeile um ein Byte, dritte um zwei Byte und vierte um drei Byte nach rechts.
     * In der for-Schleife wird zunächst eine temporäres Array erstellt. Daraufhin wird in der nächsten for-Schleife
     * die verschobene/rotierte Spaltenposition errechnet. Der Inhalt der state Matrix an aktueller Stelle wird
     * dann an diese Stelle gesetzt. Wenn die komplette Zeile durchgelaufen ist, wird der Inhalt des temporären
     * Array wieder in die state Matrix geschrieben.
     */
    for(u8 i = 0; i < MATRIX_SIZE; i++) {

        u8 tmpRow[MATRIX_SIZE];
        for(u8 j = 0; j < MATRIX_SIZE; j++) {
            u8 shiftedColumn = (j + i) % MATRIX_SIZE;
            tmpRow[shiftedColumn] = state[i][j];
        }

        for(u8 j = 0; j < MATRIX_SIZE; j++) {
            state[i][j] = tmpRow[j];
        }

    }
}

void shift_rows_inv(u8 state[4][4])
{
    /*
     * TODO: Inverse ShiftRows Operation: Schiebe zweite Zeile um ein Byte, dritte um zwei Byte und vierte um drei Byte nach links.
     * In der for-Schleife wird zunächst eine temporäres Array erstellt. Daraufhin wird in der nächsten for-Schleife
     * die verschobene/rotierte spalten Position errechnet. Der Inhalt der state Matrix an aktueller Stelle wird,
     * dann an diese Stelle gesetzt. Wenn die komplette Zeile durchgelaufen ist, wird der Inhalt des temporären
     * Array wieder in die state Matrix geschrieben.
     */
    for(u8 i = 0; i < MATRIX_SIZE; i++) {

        u8 tmpRow[MATRIX_SIZE];
        for(u8 j = 0; j < MATRIX_SIZE; j++) {
            // Fallunterscheidung hier notwendig da: -a % b != -a mod b
            u8 shiftedColumn = (j - i) < 0 ? (j - i) + MATRIX_SIZE : (j - i);
            tmpRow[shiftedColumn] = state[i][j];
        }

        for(u8 j = 0; j < MATRIX_SIZE; j++) {
            state[i][j] = tmpRow[j];
        }

    }
}

void mix_columns(u8 state[4][4])
{
    /*
     * TODO: MixColumns Operation: Multiplikation aller Spalten mit der MixColumns-Matrix M, lässt sich zu wenigen XOR-Rechnungen vereinfachen.
     * Zunächst wird die Konstante Multiplikations Matrix deklariert. 
     * Daraufhin werden in einer for-Schleife alle Spalten der state Matrix 
     * durchgegangen und jeweils mit der Multiplikations Matrix multipliziert.
     */ 
    const u8 M_TBL[MATRIX_SIZE][MATRIX_SIZE] = {{1, 0, 1, 1}, 
                                                {1, 0, 0, 0}, 
                                                {0, 1, 1, 0}, 
                                                {1, 0, 1, 0}};

    for(u8 i = 0; i < MATRIX_SIZE; i++) {
        /*
         * Es wird ein temporäres Array zum speichern der neuen Spalte erstellt.
         * Danach werden die einzelnen Bytes der neuen Spalte berechnet indem alle Bytes der
         * ursprünglichen Spalte mit dem Wert der entsprechenden Position der
         * Multiplikations Matrix multipliziert und mit dem aktuellen
         * Byte in der neuen Spalte ver-XOR-t.
         */
        u8 newColumn[] = {0, 0, 0, 0};
        for(u8 j = 0; j < MATRIX_SIZE; j++) {
            for(u8 k = 0; k < MATRIX_SIZE; k++) {
                newColumn[j] ^= state[k][i] * M_TBL[j][k];
            }
        }
        // Die neu berechnete Spalte ersetzt die jeweilige alte Spalte in der state Matrix
        for(u8 j = 0; j < MATRIX_SIZE; j++) {
            state[j][i] = newColumn[j];
        }

    }
}

void mix_columns_inv(u8 state[4][4])
{
    /*
     * TODO: Inverse MixColumns Operation: Multiplikation aller Spalten mit der inversen MixColumns-Matrix M^{-1}, lässt sich zu wenigen XOR-Rechnungen vereinfachen.
     * Zunächst wird die Konstante inversen Multiplikations Matrix deklariert. 
     * Daraufhin werden in einer for-Schleife alle Spalten der state Matrix 
     * durchgegangen und jeweils mit der Multiplikations Matrix multipliziert.
     */ 
    const u8 M_TBL[MATRIX_SIZE][MATRIX_SIZE] = {{0, 1, 0, 0},
                                                {0, 1, 1, 1}, 
                                                {0, 1, 0, 1}, 
                                                {1, 0, 0, 1}};

    for(u8 i = 0; i < MATRIX_SIZE; i++) {
        /*
         * Es wird ein temporäres Array zum speichern der neuen Spalte erstellt.
         * Danach werden die einzelnen Bytes der neuen Spalte berechnet indem alle Bytes der
         * ursprünglichen Spalte mit dem Wert der entsprechenden Position der
         * inversen Multiplikations Matrix multipliziert und mit dem aktuellen
         * Byte in der neuen Spalte ver-XOR-t.
         */
        u8 newColumn[] = {0, 0, 0, 0};
        for(u8 j = 0; j < MATRIX_SIZE; j++) {
            for(u8 k = 0; k < MATRIX_SIZE; k++) {
                newColumn[j] ^= state[k][i] * M_TBL[j][k];
            }
        }
        // Die neu berechnete Spalte ersetzt die jeweilige alte Spalte in der state Matrix
        for(u8 j = 0; j < MATRIX_SIZE; j++) {
            state[j][i] = newColumn[j];
        }
        
    }
}

void encrypt(const u8 plaintext[16], const u8 key[48], u8 ciphertext[16])
{
    i32 i;

    u8 state[4][4];
    u8 key_tmp[3][4][4];

    for (i = 0; i < 16; i++)
    {
        // Klartext in initialen Zustand schreiben
        state[i >> 2][i & 0x3] = plaintext[i] & 0xFF;

        // Schlüssel in temporäres Array schreiben, da dieser in der AddRoundkeys Operation verändert wird
        key_tmp[0][i >> 2][i & 0x3] = key[i] & 0xFF;
        key_tmp[1][i >> 2][i & 0x3] = key[i + 16] & 0xFF;
        key_tmp[2][i >> 2][i & 0x3] = key[i + 32] & 0xFF;
    }

    // TODO: Ausführen der Rundenoperation (56 Runden)
    for(i = 0; i < NUM_OF_ROUNDS; i++) {
        sub_cells(state);

        add_constants(state, i);

        add_roundkey(state, key_tmp);

        shift_rows(state);

        mix_columns(state);
    }


    for (i = 0; i < 16; i++)
    {
        // Finalen Zustand in Chiffrat schreiben
        ciphertext[i] = state[i >> 2][i & 0x3] & 0xFF;
    }
}

void decrypt(const u8 ciphertext[16], const u8 key[48], u8 plaintext[16])
{
    i32 i;

    u8 state[4][4];
    u8 key_tmp[3][4][4];
    u8 dummy[4][4] = {{0}};

    for (i = 0; i < 16; i++)
    {
        // Chiffrat in initialen Zustand schreiben
        state[i >> 2][i & 0x3] = ciphertext[i] & 0xFF;

        // Schlüssel in temporäres Array schreiben, da dieser in der AddRoundkeys Operation verändert wird
        key_tmp[0][i >> 2][i & 0x3] = key[i] & 0xFF;
        key_tmp[1][i >> 2][i & 0x3] = key[i + 16] & 0xFF;
        key_tmp[2][i >> 2][i & 0x3] = key[i + 32] & 0xFF;
    }

    // TODO: Schlüsselfahrplan einmal vorwärts rechnen, um den letzten Rundenschlüssel zu erhalten (vom letzten Rundenschlüssel ausgehend wird später rückwärts gerechnet)
    for(i = 0; i < NUM_OF_ROUNDS; i++) {

        add_roundkey(dummy, key_tmp);

    }
    // TODO: Ausführen der inversen Rundenoperation (56 Runden)

    for(i = NUM_OF_ROUNDS - 1; i >= 0; i--) {
        mix_columns_inv(state);

        shift_rows_inv(state);

        add_roundkey_inv(state, key_tmp);

        add_constants(state, i);

        sub_cells_inv(state);
    }


    for (i = 0; i < 16; i++)
    {
        // Finalen Zustand in Klartext schreiben
        plaintext[i] = state[i >> 2][i & 0x3] & 0xFF;
    }
}