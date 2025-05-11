from processors import start, filters, formatters, output

processor_registry = {
    "processors.start.tag_lines": start.tag_lines,
    "processors.filters.only_error": filters.only_error,
    "processors.filters.only_warn": filters.only_warn,
    "processors.formatters.snakecase": formatters.snakecase,
    "processors.output.terminal": output.terminal,
}
