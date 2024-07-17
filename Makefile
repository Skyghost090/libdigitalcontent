# Definindo variáveis
CXX = g++
CXXFLAGS = -fPIC -Wall -Wextra
LDFLAGS = -shared
TARGET_LIB = libdigitalcontent.so
TARGET_EXEC = deamon
INSTALL_DIR = /usr/share/libdigitalcontent

# Alvo padrão
all: $(TARGET_LIB) $(TARGET_EXEC) install

# Compilar a biblioteca compartilhada
$(TARGET_LIB): libdigitalcontent.cpp
	$(CXX) $(CXXFLAGS) $(LDFLAGS) -o $@ $^

# Compilar o executável
$(TARGET_EXEC): deamon.cpp
	$(CXX) -o $@ $^

# Instalar o executável no diretório de destino
install: $(TARGET_EXEC)
	sudo mkdir -p $(INSTALL_DIR)
	sudo cp $(TARGET_EXEC) $(INSTALL_DIR)

# Limpar arquivos gerados pela compilação
clean:
	rm -f $(TARGET_LIB) $(TARGET_EXEC)

.PHONY: all clean install
