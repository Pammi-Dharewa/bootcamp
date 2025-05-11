# Final Write-Up: Real-Time File Processing System

---

##  **1. Design Decisions**

The most important architectural choice for this system was its modular design, which allowed flexibility and scalability as we dealt with processing files in real-time. By using separate components for file monitoring (`monitor_folder`), processing (`example_pipeline`), and the FastAPI web dashboard, I could ensure that each part of the system was focused on a specific responsibility. This design follows the **Separation of Concerns (SoC)** principle, making it easier to maintain and extend. The use of a simple folder-based queue structure to move files between `unprocessed/`, `underprocess/`, and `processed/` directories provided a robust yet simple way of tracking the files’ states and handling failures or retries.

One abstraction that helped the most was the **file processing pipeline**, specifically the wrapper function used to add tracing capabilities. This abstraction allowed me to modify or add new processing steps easily while keeping the logic simple. The ability to monitor and track state changes in real-time with FastAPI made the system more observable and fault-tolerant.

---

##  **2. Tradeoffs**

One key tradeoff was between simplicity and fault tolerance. I prioritized making the system lightweight and easy to understand, which led to some compromises. For example, I opted not to implement complex retry logic or to add sophisticated error logging. While this keeps the code clean and focused, it also limits the system's ability to handle catastrophic failures, such as processing interruptions that might require advanced state recovery.

Another tradeoff was in the **file monitoring** mechanism, which checks the `unprocessed/` folder at regular intervals. This polling approach can work for small-scale systems, but for a large number of files, it might become inefficient. An event-driven approach, such as using file system notifications (e.g., `inotify` on Linux), would be more efficient but would add complexity.

Current limitations include the absence of real-time error handling, lack of advanced logging, and the fact that the file processing system is single-threaded. Although it can process one file at a time, it doesn’t scale well for larger loads or high-throughput environments.

---

##  **3. Scalability**

If the input volume were 100x larger, several adjustments would be necessary:

1. **File Queues**: To handle a higher volume of files, I would move from a directory-based queue to a more scalable, message-driven system. Technologies like **Apache Kafka** or **RabbitMQ** could provide more reliable handling of large numbers of incoming files.

2. **Parallelism**: The current system processes files sequentially, which would be inefficient for a large-scale use case. I would implement parallel processing using threading or multiprocessing in Python. Using a **thread pool** or **worker nodes** would help distribute the load, ensuring that multiple files can be processed simultaneously without overwhelming the system.

3. **Scaling FastAPI**: The FastAPI dashboard would need to be deployed on multiple instances to handle increased traffic for monitoring and trace requests. **Docker** and **Kubernetes** would be helpful for deploying the application in a containerized environment to support horizontal scaling.

---

## 🔐 **4. Extensibility & Security**

To run this system for real users, there are a few key things that need to be added or improved:

1. **User Authentication**: For real-world deployments, a proper user authentication and authorization system is necessary to restrict access to the monitoring dashboard. **OAuth** or **JWT tokens** could be used to secure the endpoints.

2. **Security for File Uploads**: To secure file uploads, we would need to implement file validation mechanisms, such as checking file types, size limits, and scanning for potential malicious content. This could be done using file type checks (e.g., MIME type) and integrating third-party antivirus libraries. Additionally, uploading files over **HTTPS** would ensure secure data transmission.

3. **Data Encryption**: Any sensitive data or files should be encrypted both at rest (in the file system) and in transit (while being uploaded or processed). Using **AES** encryption for file storage and ensuring HTTPS for all communications would be a good practice.

4. **Error Handling**: A robust logging and error-handling mechanism is needed for production deployments. This would include logging errors, warnings, and system health checks. I would integrate a centralized logging solution like **ELK Stack** (Elasticsearch, Logstash, Kibana) or **Prometheus** for monitoring.

---

## Conclusion

This project has provided valuable insights into building a scalable, real-time file processing system with observable and fault-tolerant architecture. While there are areas for improvement, especially around scalability and security, the system is flexible and can be extended with additional features like parallel processing, secure file uploads, and user authentication for a production-ready deployment.
