import os
import sys
import datetime
import argparse

def get_env_var(name, default):
    return os.environ.get(name, default)

def ensure_tag_exists(vault_path, tag_name, parent_tag=None):
    """
    Asegura que un archivo de etiqueta existe en la carpeta '3 - Etiquetas'.
    """
    tags_folder = os.path.join(vault_path, "3 - Etiquetas")
    if not os.path.exists(tags_folder):
        os.makedirs(tags_folder)

    tag_file_path = os.path.join(tags_folder, f"{tag_name}.md")
    
    if not os.path.exists(tag_file_path):
        content = f"{tag_name}\n"
        if parent_tag:
            content += f"[[{parent_tag}]]\n"
        
        with open(tag_file_path, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"Etiqueta creada: {tag_file_path}")

def save_to_obsidian(vault_path, unit_number, subject_name, block_name, content, course_name, root_tag):
    """
    Guarda el contenido en la bóveda de Obsidian con el formato de etiquetas jerárquicas.
    """
    # 1. Definir etiquetas
    subject_tag = subject_name
    unit_tag = f"Unidad {unit_number} - {subject_tag}"
    
    # 2. Asegurar que las etiquetas existen en '3 - Etiquetas'
    # Usar root_tag desde la configuración
    ensure_tag_exists(vault_path, subject_tag, root_tag)
    # Luego la de la unidad (padre: asignatura)
    ensure_tag_exists(vault_path, unit_tag, subject_tag)

    # 3. Crear estructura de carpetas para la nota de estudio
    safe_subject = subject_name.replace(" ", "_").replace("/", "-")
    folder_path = os.path.join(vault_path, course_name, f"Unidad_{unit_number}_{safe_subject}")
    
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

    # 4. Definir nombre de archivo de la nota
    safe_block = block_name.replace(" ", "_").replace("/", "-")
    file_name = f"{safe_block}.md"
    full_path = os.path.join(folder_path, file_name)

    # 5. Preparar formato solicitado por el usuario
    note_content = f"{block_name}\n"
    note_content += f"Tags: [[{unit_tag}]]\n"
    note_content += "---\n"
    note_content += content

    # 6. Escribir archivo
    try:
        with open(full_path, "w", encoding="utf-8") as f:
            f.write(note_content)
        return f"Éxito: Nota guardada en {full_path}"
    except Exception as e:
        return f"Error al guardar: {str(e)}"

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Guardar notas en Obsidian con jerarquía de etiquetas")
    parser.add_argument("--vault", required=True, help="Ruta de la bóveda")
    parser.add_argument("--unit_num", required=True, help="Número de la unidad")
    parser.add_argument("--subject", required=True, help="Nombre de la asignatura")
    parser.add_argument("--block", required=True, help="Nombre del bloque")
    parser.add_argument("--content", required=True, help="Contenido Markdown")
    parser.add_argument("--course", default="Master_IA", help="Nombre del curso")
    parser.add_argument("--root_tag", default="Inteligencia Artificial", help="Etiqueta raíz")

    args = parser.parse_args()
    result = save_to_obsidian(args.vault, args.unit_num, args.subject, args.block, args.content, args.course, args.root_tag)
    print(result)
