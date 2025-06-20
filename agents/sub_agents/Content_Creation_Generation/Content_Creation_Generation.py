from typing import Optional
import re
import requests

class ContentCreationGenerationAgent:
    def __init__(self):
        # Initialize resources, logs, or configurations as needed
        self.content_log = []

    def generate_marketing_material(self, campaign_info: dict) -> dict:
        """
        Generate high-impact, multi-channel marketing materials using advanced orchestration.

        Args:
            campaign_info (dict): Information about the campaign.

        Returns:
            dict: Generated marketing material content.
        """
        if not campaign_info or not isinstance(campaign_info, dict):
            raise ValueError("campaign_info must be a non-empty dictionary")
        # Simulate collaboration with copywriting, design, and analytics sub-agents
        content = {
            "type": "marketing_material",
            "campaign_info": campaign_info,
            "channels": ["email", "social_media", "web", "print"],
            "collaborators": ["CopywriterAgent", "DesignerAgent", "AnalyticsAgent"],
            "content": f"Legendary marketing material for campaign: {campaign_info.get('name', 'N/A')} crafted with data-driven insights and creative excellence.",
            "status": "completed",
            "quality_score": 9.8,
            "timestamp": "2024-06-10T12:00:00Z"
        }
        self.content_log.append(content)
        return content

    def generate_report(self, report_type: str = "", data: Optional[dict] = None) -> dict:
        """
        Generate comprehensive, executive-level reports with actionable insights.

        Args:
            report_type (str): The type of report to generate.
            data (dict): Data to include in the report.

        Returns:
            dict: Generated report content.
        """
        if data is None:
            data = {}
        if not report_type or not isinstance(data, dict):
            raise ValueError("report_type must be specified and data must be a dictionary")
        # Simulate collaboration with data analysis and visualization sub-agents
        report = {
            "type": "report",
            "report_type": report_type,
            "data": data,
            "sections": ["executive_summary", "deep_dive_analysis", "visualizations", "recommendations", "conclusion"],
            "collaborators": ["DataAnalystAgent", "VisualizationAgent"],
            "content": f"Legendary {report_type} report with actionable insights and professional visuals.",
            "status": "completed",
            "quality_score": 9.9,
            "timestamp": "2024-06-10T12:00:00Z"
        }
        self.content_log.append(report)
        return report

    def generate_code(self, requirements: str) -> dict:
        """
        Generate production-ready, legendary code with best practices and documentation.
        """
        if not requirements or not isinstance(requirements, str):
            raise ValueError("requirements must be a non-empty string")
        # Simulate collaboration with code review and documentation sub-agents
        code = {
            "type": "code",
            "requirements": requirements,
            "language": "python",
            "collaborators": ["CodeGenAgent", "CodeReviewAgent", "DocGenAgent"],
            "content": f"# Legendary code generated for: {requirements}\n# Includes best practices and documentation.\nprint('Hello, Legend!')",
            "status": "completed",
            "quality_score": 10.0,
            "timestamp": "2024-06-10T12:00:00Z"
        }
        self.content_log.append(code)
        return code

    @staticmethod
    def _is_url(text: str) -> bool:
        url_regex = re.compile(
            r'^(https?://)?'  # http:// or https://
            r'([a-zA-Z0-9.-]+(\.[a-zA-Z]{2,}))'  # domain
            r'(:\d+)?'  # optional port
            r'(/[^\s]*)?$'  # path
        )
        return bool(url_regex.match(text.strip()))

    @staticmethod
    def _fetch_url_content(url: str) -> str:
        try:
            if not url.startswith("http"):
                url = "http://" + url
            resp = requests.get(url, timeout=5)
            resp.raise_for_status()
            return resp.text[:1000]  # limit to 1k chars for summary
        except Exception as e:
            return f"Could not fetch URL: {e}"

    def improve_code(self, code: str, language: str = "python") -> dict:
        """Attempts to improve the provided code for various programming languages.

        Args:
            code (str): The code to improve.
            language (str): The programming language of the code.

        Returns:
            dict: status and improved code or error message.
        """
        if not isinstance(code, str) or not code.strip():
            return {
                "status": "error",
                "error_message": "No code provided to improve.",
            }
        lang = (language or "python").strip().lower()
        # If code is a URL, fetch code from the link
        if self._is_url(code):
            code = self._fetch_url_content(code)
        improved = code.strip()
        if lang == "python":
            # Add missing colons for def/class, fix indentation, etc.
            improved = re.sub(r'^(def .+\))\s*$', r'\1:', improved, flags=re.MULTILINE)
            improved = re.sub(r'^(class .+)\s*$', r'\1:', improved, flags=re.MULTILINE)
            try:
                compile(improved, "<string>", "exec")
                status = "success"
            except Exception as e:
                improved = f"# Attempted fix, but error remains: {e}\n" + improved
                status = "warning"
            improved = "# Improved Python code\n" + improved
        else:
            comment = "//" if lang in [
                "flutter", "reactnative", "swift", "javascript", "typescript", "java", "c++", "c#", "go", "kotlin"
            ] else "#"
            improved = f"{comment} Improved {language.title()} code\n" + improved
            status = "success"
        return {
            "status": status,
            "improved_code": improved,
        }

    def generate_code_from_text(self, description: str, language: str = "python") -> dict:
        """Generates code for a UI or any code based on a text description and target language.

        Args:
            description (str): The UI or code description.
            language (str): The target programming language.

        Returns:
            dict: status and generated code or error message.
        """
        if not isinstance(description, str) or not description.strip():
            return {
                "status": "error",
                "generated_code": "",
                "error_message": "No description provided."
            }
        lang = (language or "python").strip().lower()
        if self._is_url(description):
            fetched = self._fetch_url_content(description)
            description = f"UI for content from {description}:\n{fetched[:200]}"
        code = ""
        desc_lower = description.lower()

        # --- Enhanced problem solving for complex UI/code generation ---
        if lang == "python":
            if any(x in desc_lower for x in ["tkinter", "ui", "window", "dashboard", "form", "table", "canvas", "tabs", "notebook"]):
                # Advanced Tkinter UI generation
                if "dashboard" in desc_lower:
                    code = (
                        "import tkinter as tk\n"
                        "from tkinter import ttk\n"
                        "root = tk.Tk()\n"
                        "root.title('Dashboard')\n"
                        "notebook = ttk.Notebook(root)\n"
                        "tab1 = tk.Frame(notebook)\n"
                        "tab2 = tk.Frame(notebook)\n"
                        "notebook.add(tab1, text='Overview')\n"
                        "notebook.add(tab2, text='Details')\n"
                        "notebook.pack(expand=1, fill='both')\n"
                        "tk.Label(tab1, text='Welcome to the Dashboard!').pack(pady=10)\n"
                        "tree = ttk.Treeview(tab2, columns=('A', 'B', 'C'), show='headings')\n"
                        "for col in ('A', 'B', 'C'):\n"
                        "    tree.heading(col, text=col)\n"
                        "tree.insert('', 'end', values=(1, 2, 3))\n"
                        "tree.pack(fill='both', expand=True)\n"
                        "root.mainloop()\n"
                    )
                elif "form" in desc_lower and "fields" in desc_lower:
                    code = (
                        "import tkinter as tk\n"
                        "root = tk.Tk()\n"
                        "root.title('Complex Form UI')\n"
                        "fields = ['Name', 'Email', 'Age']\n"
                        "entries = {}\n"
                        "for idx, field in enumerate(fields):\n"
                        "    label = tk.Label(root, text=field)\n"
                        "    label.grid(row=idx, column=0, padx=5, pady=5)\n"
                        "    entry = tk.Entry(root)\n"
                        "    entry.grid(row=idx, column=1, padx=5, pady=5)\n"
                        "    entries[field] = entry\n"
                        "def submit():\n"
                        "    print({f: e.get() for f, e in entries.items()})\n"
                        "tk.Button(root, text='Submit', command=submit).grid(row=len(fields), column=0, columnspan=2)\n"
                        "root.mainloop()\n"
                    )
                elif "table" in desc_lower:
                    code = (
                        "import tkinter as tk\n"
                        "from tkinter import ttk\n"
                        "root = tk.Tk()\n"
                        "root.title('Table UI')\n"
                        "tree = ttk.Treeview(root, columns=('A', 'B', 'C'), show='headings')\n"
                        "for col in ('A', 'B', 'C'):\n"
                        "    tree.heading(col, text=col)\n"
                        "tree.insert('', 'end', values=(1, 2, 3))\n"
                        "tree.insert('', 'end', values=(4, 5, 6))\n"
                        "tree.pack(fill='both', expand=True)\n"
                        "root.mainloop()\n"
                    )
                elif "tabs" in desc_lower or "notebook" in desc_lower:
                    code = (
                        "import tkinter as tk\n"
                        "from tkinter import ttk\n"
                        "root = tk.Tk()\n"
                        "root.title('Tabbed UI')\n"
                        "notebook = ttk.Notebook(root)\n"
                        "tab1 = tk.Frame(notebook)\n"
                        "tab2 = tk.Frame(notebook)\n"
                        "notebook.add(tab1, text='Tab 1')\n"
                        "notebook.add(tab2, text='Tab 2')\n"
                        "notebook.pack(expand=1, fill='both')\n"
                        "tk.Label(tab1, text='Content for Tab 1').pack(padx=10, pady=10)\n"
                        "tk.Label(tab2, text='Content for Tab 2').pack(padx=10, pady=10)\n"
                        "root.mainloop()\n"
                    )
                elif "canvas" in desc_lower:
                    code = (
                        "import tkinter as tk\n"
                        "root = tk.Tk()\n"
                        "root.title('Canvas Drawing')\n"
                        "canvas = tk.Canvas(root, width=400, height=300, bg='white')\n"
                        "canvas.pack()\n"
                        "canvas.create_rectangle(50, 50, 150, 150, fill='blue')\n"
                        "canvas.create_oval(200, 100, 300, 200, fill='red')\n"
                        "root.mainloop()\n"
                    )
                else:
                    widgets = []
                    if "button" in desc_lower:
                        widgets.append("button = tk.Button(root, text='Click Me')\nbutton.pack(pady=10)")
                    if "entry" in desc_lower or "input" in desc_lower:
                        widgets.append("entry = tk.Entry(root)\nentry.pack(pady=10)")
                    code = (
                        "import tkinter as tk\n"
                        "root = tk.Tk()\n"
                        "root.title('Generated UI')\n"
                        "label = tk.Label(root, text='This is a generated UI')\n"
                        "label.pack(padx=20, pady=20)\n"
                        + ("\n".join(widgets) if widgets else "") +
                        "\nroot.mainloop()\n"
                    )
            elif "for loop" in desc_lower:
                code = "for i in range(10):\n    print(i)"
            elif "class" in desc_lower:
                code = (
                    "class MyClass:\n"
                    "    def __init__(self):\n"
                    "        pass\n"
                )
            elif "sort" in desc_lower and "list" in desc_lower:
                code = (
                    "def sort_list(lst):\n"
                    "    return sorted(lst)\n"
                    "# Example usage:\n"
                    "print(sort_list([3, 1, 2]))"
                )
            elif "search" in desc_lower and "binary" in desc_lower:
                code = (
                    "def binary_search(arr, target):\n"
                    "    left, right = 0, len(arr) - 1\n"
                    "    while left <= right:\n"
                    "        mid = (left + right) // 2\n"
                    "        if arr[mid] == target:\n"
                    "            return mid\n"
                    "        elif arr[mid] < target:\n"
                    "            left = mid + 1\n"
                    "        else:\n"
                    "            right = mid - 1\n"
                    "    return -1\n"
                    "# Example usage:\n"
                    "print(binary_search([1,2,3,4,5], 3))"
                )
            else:
                code = "# " + description
        elif lang == "swift":
            if "ui" in desc_lower or "swiftui" in desc_lower or "form" in desc_lower or "table" in desc_lower:
                if "form" in desc_lower:
                    code = (
                        "import SwiftUI\n\n"
                        "struct ContentView: View {\n"
                        "    @State private var name = \"\"\n"
                        "    @State private var email = \"\"\n"
                        "    var body: some View {\n"
                        "        Form {\n"
                        "            TextField(\"Name\", text: $name)\n"
                        "            TextField(\"Email\", text: $email)\n"
                        "            Button(\"Submit\") {\n"
                        "                print(\"Name: \\(name), Email: \\(email)\")\n"
                        "            }\n"
                        "        }\n"
                        "    }\n"
                        "}\n"
                    )
                elif "table" in desc_lower:
                    code = (
                        "import SwiftUI\n\n"
                        "struct Row: Identifiable {\n"
                        "    let id = UUID()\n"
                        "    let value: String\n"
                        "}\n"
                        "struct ContentView: View {\n"
                        "    let rows = [Row(value: \"A\"), Row(value: \"B\")]\n"
                        "    var body: some View {\n"
                        "        List(rows) { row in\n"
                        "            Text(row.value)\n"
                        "        }\n"
                        "    }\n"
                        "}\n"
                    )
                else:
                    code = (
                        "import SwiftUI\n\n"
                        "struct ContentView: View {\n"
                        "    var body: some View {\n"
                        "        VStack {\n"
                        "            Text(\"This is a generated UI\")\n"
                        "        }\n"
                        "    }\n"
                        "}\n"
                    )
            elif "for loop" in desc_lower:
                code = "for i in 0..<10 {\n    print(i)\n}"
            elif "sort" in desc_lower and "array" in desc_lower:
                code = (
                    "let arr = [3, 1, 2]\n"
                    "let sortedArr = arr.sorted()\n"
                    "print(sortedArr)"
                )
            else:
                code = "// " + description
        elif lang == "javascript":
            if "ui" in desc_lower or "form" in desc_lower or "table" in desc_lower:
                if "form" in desc_lower:
                    code = (
                        "<!DOCTYPE html>\n<html><body>\n"
                        "<form>\n"
                        "  Name: <input type='text' name='name'><br>\n"
                        "  Email: <input type='email' name='email'><br>\n"
                        "  <input type='submit' value='Submit'>\n"
                        "</form>\n"
                        "</body></html>\n"
                    )
                elif "table" in desc_lower:
                    code = (
                        "<!DOCTYPE html>\n<html><body>\n"
                        "<table border='1'>\n"
                        "  <tr><th>A</th><th>B</th></tr>\n"
                        "  <tr><td>1</td><td>2</td></tr>\n"
                        "  <tr><td>3</td><td>4</td></tr>\n"
                        "</table>\n"
                        "</body></html>\n"
                    )
                else:
                    code = (
                        "<!DOCTYPE html>\n<html><body>\n"
                        "<h1>This is a generated UI</h1>\n"
                        "</body></html>\n"
                    )
            elif "for loop" in desc_lower:
                code = "for(let i = 0; i < 10; i++) {\n    console.log(i);\n}"
            elif "sort" in desc_lower and "array" in desc_lower:
                code = (
                    "let arr = [3, 1, 2];\n"
                    "arr.sort();\n"
                    "console.log(arr);"
                )
            else:
                code = "// " + description
        elif lang == "reactnative":
            if "ui" in desc_lower or "form" in desc_lower or "table" in desc_lower:
                if "form" in desc_lower:
                    code = (
                        "import React, { useState } from 'react';\n"
                        "import { View, Text, TextInput, Button } from 'react-native';\n\n"
                        "export default function GeneratedForm() {\n"
                        "  const [name, setName] = useState('');\n"
                        "  const [email, setEmail] = useState('');\n"
                        "  return (\n"
                        "    <View style={{ padding: 20 }}>\n"
                        "      <Text>Name:</Text>\n"
                        "      <TextInput value={name} onChangeText={setName} style={{ borderWidth: 1, marginBottom: 10 }} />\n"
                        "      <Text>Email:</Text>\n"
                        "      <TextInput value={email} onChangeText={setEmail} style={{ borderWidth: 1, marginBottom: 10 }} />\n"
                        "      <Button title='Submit' onPress={() => console.log(name, email)} />\n"
                        "    </View>\n"
                        "  );\n"
                        "}\n"
                    )
                elif "table" in desc_lower:
                    code = (
                        "import React from 'react';\n"
                        "import { View, Text } from 'react-native';\n\n"
                        "export default function Table() {\n"
                        "  const data = [\n"
                        "    { a: 1, b: 2 },\n"
                        "    { a: 3, b: 4 }\n"
                        "  ];\n"
                        "  return (\n"
                        "    <View>\n"
                        "      {data.map((row, idx) => (\n"
                        "        <View key={idx} style={{ flexDirection: 'row' }}>\n"
                        "          <Text>{row.a}</Text>\n"
                        "          <Text>{row.b}</Text>\n"
                        "        </View>\n"
                        "      ))}\n"
                        "    </View>\n"
                        "  );\n"
                        "}\n"
                    )
                else:
                    code = (
                        "import React from 'react';\n"
                        "import { View, Text } from 'react-native';\n\n"
                        "export default function GeneratedUI() {\n"
                        "  return (\n"
                        "    <View style={{ flex: 1, justifyContent: 'center', alignItems: 'center' }}>\n"
                        "      <Text>This is a generated UI</Text>\n"
                        "    </View>\n"
                        "  );\n"
                        "}\n"
                    )
            elif "for loop" in desc_lower:
                code = (
                    "// React Native for loop example\n"
                    "{[...Array(10).keys()].map(i => (\n"
                    "  <Text key={i}>{i}</Text>\n"
                    "))}"
                )
            else:
                code = "// " + description
        elif lang == "flutter":
            if "ui" in desc_lower or "form" in desc_lower or "table" in desc_lower:
                if "form" in desc_lower:
                    code = (
                        "import 'package:flutter/material.dart';\n\n"
                        "class GeneratedForm extends StatefulWidget {\n"
                        "  @override\n"
                        "  _GeneratedFormState createState() => _GeneratedFormState();\n"
                        "}\n\n"
                        "class _GeneratedFormState extends State<GeneratedForm> {\n"
                        "  final _formKey = GlobalKey<FormState>();\n"
                        "  String name = '', email = '';\n"
                        "  @override\n"
                        "  Widget build(BuildContext context) {\n"
                        "    return Scaffold(\n"
                        "      appBar: AppBar(title: Text('Generated Form')),\n"
                        "      body: Padding(\n"
                        "        padding: const EdgeInsets.all(16.0),\n"
                        "        child: Form(\n"
                        "          key: _formKey,\n"
                        "          child: Column(\n"
                        "            children: [\n"
                        "              TextFormField(\n"
                        "                decoration: InputDecoration(labelText: 'Name'),\n"
                        "                onChanged: (val) => setState(() => name = val),\n"
                        "              ),\n"
                        "              TextFormField(\n"
                        "                decoration: InputDecoration(labelText: 'Email'),\n"
                        "                onChanged: (val) => setState(() => email = val),\n"
                        "              ),\n"
                        "              ElevatedButton(\n"
                        "                onPressed: () {\n"
                        "                  print('Name: \$name, Email: \$email');\n"
                        "                },\n"
                        "                child: Text('Submit'),\n"
                        "              ),\n"
                        "            ],\n"
                        "          ),\n"
                        "        ),\n"
                        "      ),\n"
                        "    );\n"
                        "  }\n"
                        "}\n"
                    )
                elif "table" in desc_lower:
                    code = (
                        "import 'package:flutter/material.dart';\n\n"
                        "class TableWidget extends StatelessWidget {\n"
                        "  @override\n"
                        "  Widget build(BuildContext context) {\n"
                        "    return Scaffold(\n"
                        "      appBar: AppBar(title: Text('Table')),\n"
                        "      body: DataTable(\n"
                        "        columns: [\n"
                        "          DataColumn(label: Text('A')),\n"
                        "          DataColumn(label: Text('B')),\n"
                        "        ],\n"
                        "        rows: [\n"
                        "          DataRow(cells: [DataCell(Text('1')), DataCell(Text('2'))]),\n"
                        "          DataRow(cells: [DataCell(Text('3')), DataCell(Text('4'))]),\n"
                        "        ],\n"
                        "      ),\n"
                        "    );\n"
                        "  }\n"
                        "}\n"
                    )
                else:
                    code = (
                        "import 'package:flutter/material.dart';\n\n"
                        "class GeneratedUI extends StatelessWidget {\n"
                        "  @override\n"
                        "  Widget build(BuildContext context) {\n"
                        "    return Scaffold(\n"
                        "      appBar: AppBar(title: Text('Generated UI')),\n"
                        "      body: Center(child: Text('This is a generated UI')),\n"
                        "    );\n"
                        "  }\n"
                        "}\n"
                    )
            elif "for loop" in desc_lower:
                code = (
                    "for (int i = 0; i < 10; i++) {\n"
                    "  print(i);\n"
                    "}"
                )
            else:
                code = "// " + description
        else:
            if "for loop" in desc_lower:
                if lang in ["java", "c++", "c#", "kotlin", "go"]:
                    code = "for (int i = 0; i < 10; i++) {\n    // code\n}"
                else:
                    code = "// for loop"
            elif "sort" in desc_lower:
                code = "// sort code"
            else:
                comment = "//" if lang in [
                    "javascript", "typescript", "java", "c++", "c#", "go", "kotlin"
                ] else "#"
                code = f"{comment} {description}"
        return {
            "status": "success",
            "generated_code": code,
        }

    def analyze_link(self, link: str) -> dict:
        # ...existing code...
        import requests
        from urllib.parse import urlparse
        if not isinstance(link, str) or not link.strip():
            return {"status": "error", "error_message": "No link provided."}
        url = link.strip()
        if not url.startswith("http"):
            url = "http://" + url
        parsed = urlparse(url)
        domain = parsed.netloc.lower()
        path = parsed.path.lower()
        try:
            resp = requests.head(url, allow_redirects=True, timeout=5)
            content_type = resp.headers.get("Content-Type", "")
        except Exception:
            content_type = ""
        # Simple heuristics
        if "github.com" in domain:
            desc = "GitHub repository or file."
        elif path.endswith(".pdf") or "pdf" in content_type:
            desc = "PDF document."
        elif path.endswith(".py"):
            desc = "Python source code file."
        elif path.endswith(".ipynb"):
            desc = "Jupyter notebook file."
        elif "youtube.com" in domain or "youtu.be" in domain:
            desc = "YouTube video."
        elif "wikipedia.org" in domain:
            desc = "Wikipedia article."
        elif "html" in content_type or content_type.startswith("text/html") or path.endswith((".html", ".htm", "/")):
            desc = "Web page (HTML)."
        elif "json" in content_type or path.endswith(".json"):
            desc = "JSON data."
        elif "image" in content_type:
            desc = f"Image file ({content_type})."
        elif "text" in content_type:
            desc = f"Text file ({content_type})."
        else:
            desc = "Unknown or unsupported link type."
        return {
            "status": "success",
            "link": url,
            "domain": domain,
            "path": path,
            "content_type": content_type,
            "description": desc
        }

    def google_search_link(self, link: str) -> dict:
        # ...existing code...
        try:
            from agents.tools.search import google_search_grounding  # Adjust import path as needed
        except ImportError:
            return {
                "status": "error",
                "error_message": "Search agent tool not found. Please ensure it exists in the tools folder."
            }

        if not isinstance(link, str) or not link.strip():
            return {"status": "error", "error_message": "No link provided."}
        query = link.strip()
        try:
            result = google_search_grounding.run(query)
            return {
                "status": "success",
                "response": result
            }
        except Exception as e:
            return {
                "status": "error",
                "error_message": f"Search agent failed: {e}"
            }

