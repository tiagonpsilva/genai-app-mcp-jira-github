"""Módulo para configuração de logging da aplicação."""

import os
import logging
from logging.handlers import RotatingFileHandler
import sys

# Configuração básica de logging
log_formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

# Define o nível de log com base na variável de ambiente DEBUG
debug_mode = os.getenv('DEBUG', 'False').lower() == 'true'
log_level = logging.DEBUG if debug_mode else logging.INFO

# Cria o diretório de logs se não existir
log_dir = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))), 'logs')
os.makedirs(log_dir, exist_ok=True)

def get_logger(name):
    """Cria e configura um logger com nome específico.
    
    Args:
        name: Nome do logger (geralmente o nome do módulo)
        
    Returns:
        Logger configurado
    """
    logger = logging.getLogger(name)
    logger.setLevel(log_level)
    
    # Evita adicionar múltiplos handlers ao mesmo logger
    if not logger.handlers:
        # Handler para enviar logs ao console
        console_handler = logging.StreamHandler(sys.stdout)
        console_handler.setFormatter(log_formatter)
        logger.addHandler(console_handler)
        
        # Handler para salvar logs em arquivo
        file_handler = RotatingFileHandler(
            os.path.join(log_dir, f'{name}.log'),
            maxBytes=1024 * 1024 * 5,  # 5 MB
            backupCount=5
        )
        file_handler.setFormatter(log_formatter)
        logger.addHandler(file_handler)
    
    return logger
