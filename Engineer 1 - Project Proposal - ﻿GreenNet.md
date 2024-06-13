### A Micro-service Based Platform for Secure User Authentication and Device Monitoring in Energy Management

**Tagline**: "Empowering Energy Efficiency through Secure and Scalable User and Device Management"

**Team**

- **Team Members:**
  - Okoyen Ebisine Precious (Project Lead, Backend Developer, Frontend Developer, UI/UX Designer)

- **Roles**:
  - Okoyen Ebisine Precious (Green): Responsible for designing and implementing the backend architecture, including the user management and device management microservices. 
  - Also responsible for designing and implementing the frontend user interface, as well as ensuring a seamless user experience.
  - Responsible for setting up and maintaining the infrastructure, including the deployment strategy and testing automation.

- **Role Decisions:**
  - Role is based on the Software Requirement Specification (SRS)
    

**Technologies**

- **Libraries and Frameworks:**
	- Python (Backend)
	- React (Frontend)
	- Docker (Containerization)
	- Kubernetes (Orchestration)
	- MongoDB (Database)

- **Alternate Technology Choices:**
	- Instead of Python, we could have chosen Node.js as the backend language. However, Python was chosen for its simplicity, flexibility, and extensive libraries.
	- Instead of React, we could have chosen Angular as the frontend framework. However, React was chosen for its flexibility and ease of use.

**Challenge Statement**
- **Problem Statement:** The lack of secure and scalable user authentication and device monitoring solutions in smart energy systems hinders the efficient management of energy resources.
- **What the Project Will Not Solve:** This project will not solve the problem of energy generation or distribution, but rather focus on the management and monitoring of energy devices.
- **Target Users:** Energy companies, utility providers, and smart grid operators.
- **Locale Dependence:** This project is not dependent on a specific locale, but can be adapted to various regions and energy systems.
    

**Risks**

- **Technical Risks:**
	- Integration of multiple microservices may lead to complexity and scalability issues.
	- Potential impact: Delayed deployment and increased maintenance costs.
	- Safeguards: Implementing a robust testing strategy and utilising containerization and orchestration tools.
    

- **Non-Technical Risks:**
	- Resistance to change from energy companies and utility providers.
	- Potential impact: Delayed adoption and reduced market share.
	- Strategies: Engaging with stakeholders early on, providing training and support, and highlighting the benefits of the ***GreenNet*** platform.
    

**Infrastructure**
- **Branching and Merging:** I will use the GitHub flow, with a main branch for production and feature branches for new developments.
- **Deployment Strategy:** I will use a containerized deployment strategy, utilising Docker and Kubernetes.
- **Data Population:** I will populate the app with sample data, and later integrate with real-world energy device data.
- **Testing**: I will use a combination of unit testing, integration testing, and end-to-end testing, utilising tools such as Jest and Cypress.
    

**Existing Solutions**
- **Similar Products:**
	- Smart energy management platforms (e.g. **African Energy Management System (AEMS) (Ghana)**)
	- IoT device management platforms (e.g. *AWS IoT Device Management*)

- **Similarities and Differences:**
	- ***GreenNet*** focuses specifically on user authentication and device monitoring, whereas existing solutions may provide a broader range of features.
	- ***GreenNet's*** micro-service architecture allows for greater scalability and flexibility compared to monolithic solutions.