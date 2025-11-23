---
name: gemini-file-upload
description: Upload documents to Gemini File Search Store. Configure chunking. Create persistent knowledge base. Use when Gemini upload, RAG setup, knowledge base creation requested.
allowed-tools: Read
---

# Gemini File Upload

## Progressive Disclosure

**Level 1** (This file): Core upload logic (~700 tokens)
**Level 2**: ERROR_HANDLING.md (~900 tokens, load if errors)

## Quick Start

1. Create File Search Store (persistent)
2. Upload documents with metadata
3. Wait for import completion
4. Return store name for global access

## Critical

Use File Search Stores (indefinite storage), NOT basic File API (48h deletion)

## When This Activates

Keywords: gemini, upload, RAG, knowledge base, file search
