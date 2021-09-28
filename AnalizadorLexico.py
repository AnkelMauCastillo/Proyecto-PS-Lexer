#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on 

 @author Angel Castillo Zavala
 @author Hazel Garcia Dominguez
 
"""
import TipoToken
import SubTipoToken
import Token


class AnalizadorLexico:

    numLinea = 1
    L = []
    codigo = ""

    def __init__(self, programa):

        archivo = open(programa, 'r')
        lineas = archivo.readlines()
        for linea in lineas:
            self.codigo = self.codigo + linea

    def obtenerToken(self):

        if len(self.L) > 0:
            return self.L.pop(0)
        return None

    def regresarToken(self, t):

        self.L.insert(0, t)

    def esPalabraReservada(self, lexeme):

        return None

    def crearLista(self):

        index = 0
       
        c = self.codigo[index]
        while (index < len(self.codigo)):
            c = self.codigo[index]

            numeros = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
            abecedario = [
                "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l",
                "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x",
                "y", "z"
            ]

            abecedarioMayus = [
                "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L",
                "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X",
                "Y", "Z"
            ] 

                                  
                

            if c in abecedario:
                if c == "l":
                    index = index + 1
                    concat = str(c)
                    if (index < len(self.codigo)):
                        c = self.codigo[index]
                        if c == "e":
                            index = index + 1
                            concat = concat + str(c)
                            if (index < len(self.codigo)):
                                c = self.codigo[index]
                                if c == "t":
                                    index = index + 1
                                    concat = concat + str(c)
                                    t = Token.Token(
                                        TipoToken.PALABRAS_RESERVADAS, None,
                                        concat, self.numLinea)
                                    self.L.append(t)
                elif c == "i":
                    index = index + 1
                    concat = str(c)
                    if (index < len(self.codigo)):
                        c = self.codigo[index]
                        if c == "f":
                            index = index + 1
                            concat = concat + str(c)
                            t = Token.Token(TipoToken.PALABRAS_RESERVADAS,
                                            None, concat, self.numLinea)
                            self.L.append(t)
                        elif c == "n":
                            index = index + 1
                            concat = concat + str(c)
                            t = Token.Token(TipoToken.PALABRAS_RESERVADAS,
                                            None, concat, self.numLinea)
                            self.L.append(t)

                elif c == "e":  # tomamos la palabra endif, else, endlet
                    index = index + 1
                    concat = str(c)
                    if (index < len(self.codigo)):
                        c = self.codigo[index]
                        if c == "l":
                            index = index + 1
                            concat = concat + str(c)
                            if (index < len(self.codigo)):
                                c = self.codigo[index]
                                if c == "s":
                                    index = index + 1
                                    concat = concat + str(c)
                                    if (index < len(self.codigo)):
                                        c = self.codigo[index]
                                        if c == "e":
                                            index = index + 1
                                            concat = concat + str(c)
                                            t = Token.Token(
                                                TipoToken.PALABRAS_RESERVADAS,
                                                None, concat, self.numLinea)
                                            self.L.append(t)
                        elif c == "n":
                            index = index + 1
                            concat = concat + str(c)
                            if (index < len(self.codigo)):
                                c = self.codigo[index]
                                if c == "d":
                                    index = index + 1
                                    concat = concat + str(c)
                                    if (index < len(self.codigo)):
                                        c = self.codigo[index]
                                        if c == "i":
                                            index = index + 1
                                            concat = concat + str(c)
                                            if (index < len(self.codigo)):
                                                c = self.codigo[index]
                                                if c == "f":
                                                    index = index + 1
                                                    concat = concat + str(c)
                                                    t = Token.Token(
                                                        TipoToken.
                                                        PALABRAS_RESERVADAS,
                                                        None, concat,
                                                        self.numLinea)
                                                    self.L.append(t)
                                        elif c == "l":
                                            index = index + 1
                                            concat = concat + str(c)
                                            if (index < len(self.codigo)):
                                                c = self.codigo[index]
                                                if c == "e":
                                                    index = index + 1
                                                    concat = concat + str(c)
                                                    if (index < len(
                                                            self.codigo)):
                                                        c = self.codigo[index]
                                                        if c == "t":
                                                            index = index + 1
                                                            concat = concat + str(
                                                                c)
                                                            t = Token.Token(
                                                                TipoToken.
                                                                PALABRAS_RESERVADAS,
                                                                None, concat,
                                                                self.numLinea)
                                                            self.L.append(t)

                elif c == "t":
                    index = index + 1
                    concat = str(c)
                    if (index < len(self.codigo)):
                        c = self.codigo[index]
                        if c == "h":
                            index = index + 1
                            concat = concat + str(c)
                            if (index < len(self.codigo)):
                                c = self.codigo[index]
                                if c == "e":
                                    index = index + 1
                                    concat = concat + str(c)
                                    if (index < len(self.codigo)):
                                        c = self.codigo[index]
                                        if c == "n":
                                            index = index + 1
                                            concat = concat + str(c)
                                            t = Token.Token(
                                                TipoToken.PALABRAS_RESERVADAS,
                                                None, concat, self.numLinea)
                                            self.L.append(t)

                else:

                                                  
                                        
                  index = index + 1
                  t = Token.Token(TipoToken.IDENTIFICADORES, None, c,
                                    self.numLinea)
                  self.L.append(t)

                  """                                  

                  if c in abecedario :
                    concat = str(c)
                    if (c in abecedario) or (c in abecedarioMayus):
                      
                      index = index + 1
                      while(index < len(self.codigo)):
                        c = self.codigo[index]
                        if c in abecedario :
                          concat = concat + str(c)
                        elif c in abecedarioMayus :
                          concat = concat + str(c)
                        elif c.isspace() == True:
                          break
                          #index = index + 1
                        index = index + 1
                      index = index + 1  
                      t = Token.Token(TipoToken.IDENTIFICADORES, None, concat, self.numLinea)
                      self.L.append(t)  
                      """
                    
                    

            if c in str(numeros):
                if c == str(0):
                    index = index + 1
                    t = Token.Token(TipoToken.NUMEROS_ENTEROS, None, c,
                                    self.numLinea)
                    self.L.append(t)
                elif c == str(1):
                    index = index + 1
                    t = Token.Token(TipoToken.NUMEROS_ENTEROS, None, c,
                                    self.numLinea)
                    self.L.append(t)
                elif c == str(2):
                    index = index + 1
                    t = Token.Token(TipoToken.NUMEROS_ENTEROS, None, c,
                                    self.numLinea)
                    self.L.append(t)
                elif c == str(3):
                    index = index + 1
                    t = Token.Token(TipoToken.NUMEROS_ENTEROS, None, c,
                                    self.numLinea)
                    self.L.append(t)
                elif c == str(4):
                    index = index + 1
                    t = Token.Token(TipoToken.NUMEROS_ENTEROS, None, c,
                                    self.numLinea)
                    self.L.append(t)
                elif c == str(5):
                    index = index + 1
                    t = Token.Token(TipoToken.NUMEROS_ENTEROS, None, c,
                                    self.numLinea)
                    self.L.append(t)
                elif c == str(6):
                    index = index + 1
                    t = Token.Token(TipoToken.NUMEROS_ENTEROS, None, c,
                                    self.numLinea)
                    self.L.append(t)
                elif c == str(7):
                    index = index + 1
                    t = Token.Token(TipoToken.NUMEROS_ENTEROS, None, c,
                                    self.numLinea)
                    self.L.append(t)
                elif c == str(8):
                    index = index + 1
                    t = Token.Token(TipoToken.NUMEROS_ENTEROS, None, c,
                                    self.numLinea)
                    self.L.append(t)
                elif c == str(9):
                    index = index + 1
                    t = Token.Token(TipoToken.NUMEROS_ENTEROS, None, c,
                                    self.numLinea)
                    self.L.append(t)

            if c in ["{", "}", "[", "]", ";", ",", ".", "(", ")"]:
                if c == "(":
                    index = index + 1
                    t = Token.Token(TipoToken.SIGNO_PUNTUACION, None, "(",
                                    self.numLinea)
                    self.L.append(t)
                elif c == ")":
                    index = index + 1
                    t = Token.Token(TipoToken.SIGNO_PUNTUACION, None, ")",
                                    self.numLinea)
                    self.L.append(t)
                elif c == "{":
                    index = index + 1
                    t = Token.Token(TipoToken.SIGNO_PUNTUACION, None, "{",
                                    self.numLinea)
                    self.L.append(t)
                elif c == "}":
                    index = index + 1
                    t = Token.Token(TipoToken.SIGNO_PUNTUACION, None, "}",
                                    self.numLinea)
                    self.L.append(t)
                elif c == "[":
                    index = index + 1
                    t = Token.Token(TipoToken.SIGNO_PUNTUACION, None, "[",
                                    self.numLinea)
                    self.L.append(t)
                elif c == "]":
                    index = index + 1
                    t = Token.Token(TipoToken.SIGNO_PUNTUACION, None, "]",
                                    self.numLinea)
                    self.L.append(t)
                elif c == ";":
                    index = index + 1
                    t = Token.Token(TipoToken.SIGNO_PUNTUACION, None, ";",
                                    self.numLinea)
                    self.L.append(t)
                elif c == ",":
                    index = index + 1
                    t = Token.Token(TipoToken.SIGNO_PUNTUACION, None, ",",
                                    self.numLinea)
                    self.L.append(t)
                elif c == ".":
                    index = index + 1
                    t = Token.Token(TipoToken.SIGNO_PUNTUACION, None, ".",
                                    self.numLinea)
                    self.L.append(t)

            #Operadores Aritmeticos
            if c in ["+", "-", "*", "/"]:
                if c == "+":
                    index = index + 1
                    t = Token.Token(TipoToken.OPERADOR_ARITMETICO, None, "+",
                                    self.numLinea)
                    self.L.append(t)
                elif c == "-":
                    index = index + 1
                    t = Token.Token(TipoToken.OPERADOR_ARITMETICO, None, "-",
                                    self.numLinea)
                    self.L.append(t)
                elif c == "*":
                    index = index + 1
                    t = Token.Token(TipoToken.OPERADOR_ARITMETICO, None, "*",
                                    self.numLinea)
                    self.L.append(t)
                else:
                    index = index + 1
                    t = Token.Token(TipoToken.OPERADOR_ARITMETICO, None, "/",
                                    self.numLinea)
                    self.L.append(t)

            if c in ["<", ">", "=", "!"]:
                if c == ">":
                    index = index + 1
                    if (index < len(self.codigo)):
                        c = self.codigo[index]
                        if c == "=":
                            index = index + 1
                            t = Token.Token(TipoToken.OPERADOR_RELACIONAL,
                                            None, ">=", self.numLinea)
                            self.L.append(t)
                        else:
                            t = Token.Token(TipoToken.OPERADOR_RELACIONAL,
                                            None, ">", self.numLinea)
                            self.L.append(t)
                if c == "<":
                    index = index + 1
                    if (index < len(self.codigo)):
                        c = self.codigo[index]
                        if c == "=":
                            index = index + 1
                            t = Token.Token(TipoToken.OPERADOR_RELACIONAL,
                                            None, "<=", self.numLinea)
                            self.L.append(t)
                        else:
                            t = Token.Token(TipoToken.OPERADOR_RELACIONAL,
                                            None, "<", self.numLinea)
                            self.L.append(t)
                if c == "=":
                    index = index + 1
                    if (index < len(self.codigo)):
                        c = self.codigo[index]
                        if c == "=":
                            index = index + 1
                            t = Token.Token(TipoToken.OPERADOR_RELACIONAL,
                                            None, "==", self.numLinea)
                            self.L.append(t)

                if c == "!":
                    index = index + 1
                    if (index < len(self.codigo)):
                        c = self.codigo[index]
                        if c == "=":
                            index = index + 1
                            t = Token.Token(TipoToken.OPERADOR_RELACIONAL,
                                            None, "!=", self.numLinea)
                            self.L.append(t)
                        else:
                            t = Token.Token(TipoToken.OPERADOR_LOGICOS, None,
                                            "!", self.numLinea)
                            self.L.append(t)

                          
            else:
              if c.isspace() == True:
                index = index + 1
              else:

                print("Error, simbolo extranio ", c)
                index = index + 1
        print("Elementos: ", len(self.L))
