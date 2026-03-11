# Technical Hook: "Encoding & Line-Ending Guard"

**Objetivo:** Prevenir la corrupción de caracteres (Mojibake) y asegurar la compatibilidad absoluta con Windows (CRLF).

**Instrucción Obligatoria:**
"Antes de realizar cualquier operación de escritura (`write_file`, `replace`):
1.  **Valida Codificación:** Asegura que el contenido sea UTF-8 puro. Prohibido el uso de codificaciones ANSI o regionales que corrompan tildes y eñes.
2.  **Valida Terminaciones:** Todas las líneas deben terminar en CRLF (`\r\n`).
3.  **Sanity Check:** Si detectas caracteres extraños (ej: `Ã©`), aborta la escritura y regenera el texto limpio."
