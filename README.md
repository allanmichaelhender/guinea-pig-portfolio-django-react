# Guinea Pig Portfolio

I created this project as a proof of concept to allow users to test portfolios before investing themselves.

## Key Focus Areas
- Primary goal I achieved: Simple and fast user experience to compute and compare potential porfolios
- Unique value I provide: Data updated daily for accurate porfolio calculations and storage of previous submissions for easy comparisons



## Live Demo

I've deployed a working version here:  
[Demo Site](https://guinea-pig-portfolio.ddnsfree.com/)) 

https://guinea-pig-portfolio.ddnsfree.com/





## My Tech Stack

**Frontend:**  
React · Vite  

**Backend:**  
Django · Django Q2 · Financial Modeling Prem API Integration

**Database:**  
PostgreSQL  

**DevOps:**  
GitHub · AWS



## My Project Structure

Here's how I organized my code:


```
backend/
├── backend/          # Django settings/setup directory
├── api/              # Main application code

frontend/
├── src/              # Main source code
│   ├── pages/        # React Pages
│   ├── components/   # React Components
```




## Deployment

Here's how I deploy this project:

Frontend
1. Install dependencies: `npm install`
2. Build production version: `npm run build`
3. Deploy the `dist` folder to AWS (or other platform)
4. Connect to Backend with VITE_API_URL environmental variable
5. Configure Nginx

Backend
1. Install dependencies: `pip install -r requirements.txt`
2. Connect database and provide DATABASE_URL environmental variable
3. Configure Financial Modeling Prep account and add API_URL to environmental variables: https://site.financialmodelingprep.com/
4. Migrate and Collect Static with django
5. Configure Gunicorn




## Data & Acknowledgements

Financial Modeling Prep is the source of all data used in computation/modeling: https://site.financialmodelingprep.com/
