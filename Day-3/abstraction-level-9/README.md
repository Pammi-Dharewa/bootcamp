# File Processing System

## How to Run Locally

To run the application locally, you can use the following command:

- For **single file mode**:

    ```bash
    python main.py --input path/to/your/file.txt
    ```

- For **watch mode** (to continuously monitor the folder):

    ```bash
    python main.py --watch
    ```

## Makefile Support

The Makefile helps with common tasks such as running the application and cleaning up build files.

1. **Run the app**:

    ```bash
    make run
    ```

2. **Build the package for distribution**:

    ```bash
    make build-package
    ```

3. **Publish the package**:

    ```bash
    make publish-package
    ```

4. **Clean up temporary and build files**:

    ```bash
    make clean
    ```

## FastAPI Endpoints

Your FastAPI dashboard exposes the following endpoints:

- `/stats`: Displays live metrics for each folder (unprocessed, underprocess, processed).
- `/trace`: Displays the current file being processed and the most recent 10 processed files.
- `/errors`: Displays the list of any errors (currently not implemented).

You can interact with these endpoints by navigating to `http://localhost:8000`.

## File Uploading

To upload files to the `unprocessed/` directory, you can use any file transfer tool (e.g., **rsync**) or integrate FastAPI file upload endpoints.

Example with **rsync**:

```
rsync -avz myfile.txt user@server:/path/to/unprocessed/
````


## Monitoring Uptime
You can monitor the uptime of the system using a free service like Better Uptime. Simply set up an uptime monitoring alert for the endpoint http://localhost:8000/health.

Notes
* Ensure you have Python 3.8+ and Docker installed.
* Make sure you have all dependencies installed by running:

```
pip install -r requirements.txt
```

## Future Enhancements
Add parallel processing for handling multiple files at once.

Add error handling and retry mechanisms for processing failures.

### 4. **Checklist**

- **Does your Makefile support all major commands?**  
  Yes, the Makefile supports building the package, running the app, cleaning, and publishing the package.

- **Can you run both one-shot and continuous modes?**  
  Yes, the CLI supports both `--input` (single file) and `--watch` (continuous monitoring).

- **Can users interact with the system via CLI, file drop, or browser?**  
  Yes, users can interact via CLI (for file processing or monitoring), file drop (via directory watch), or browser (via FastAPI dashboard).

- **Is all code committed and structured?**  
  Ensure that your code is committed to version control, and your files are structured according to best practices.

- **Is it clear how to deploy and monitor this system?**  
  Yes, the README provides clear instructions on running locally, monitoring uptime, and interacting with the FastAPI endpoints.

---









