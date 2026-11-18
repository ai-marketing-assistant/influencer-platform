<!DOCTYPE html>
<html lang="ka">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>ანიმაციური შესავალი</title>
    <style>
        body {
            margin: 0;
            height: 100vh;
            display: flex;
            flex-direction: column;
            justify-content: center;
            align-items: center;
            background-color: #0f172a; /* მუქი ფონი */
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            color: #ffffff;
        }

        /* სათაური (თავიდან სრულიად გამქრალია და ოდნავ ქვემოთაა) */
        .fade-title {
            opacity: 0;
            transform: translateY(20px);
            transition: opacity 1.5s ease, transform 1.5s ease;
            font-size: 3rem;
            font-weight: bold;
            margin-bottom: 30px;
            letter-spacing: 2px;
        }

        /* ღილაკების კონტეინერი (თავიდან სრულიად დამალულია) */
        .fade-buttons {
            opacity: 0;
            transform: translateY(20px);
            transition: opacity 1.5s ease 0.8s, transform 1.5s ease 0.8s; /* 0.8 წამიანი დაყოვნება სათაურის მერე */
            display: flex;
            gap: 15px;
        }

        /* კლასები, რომლებიც ჯავასკრიპტმა უნდა დაამატოს ანიმაციის გასააქტიურებლად */
        .show {
            opacity: 1;
            transform: translateY(0);
        }

        /* ღილაკების დიზაინი */
        .btn {
            padding: 12px 28px;
            font-size: 1rem;
            font-weight: 600;
            border: none;
            border-radius: 8px;
            cursor: pointer;
            transition: background 0.3s, transform 0.2s;
        }

        .btn-primary {
            background-color: #3b82f6;
            color: white;
        }

        .btn-primary:hover {
            background-color: #2563eb;
            transform: scale(1.05);
        }

        .btn-secondary {
            background-color: #1e293b;
            color: white;
            border: 1px solid #475569;
        }

        .btn-secondary:hover {
            background-color: #334155;
            transform: scale(1.05);
        }
    </style>
</head>
<body>

    <!-- სათაური, რომელიც ნელ-ნელა შემოვა -->
    <h1 id="mainTitle" class="fade-title">ჩემი საიტი</h1>

    <!-- ღილაკები, რომლებიც სათაურის შემდეგ გამოჩნდება -->
    <div id="actionButtons" class="fade-buttons">
        <button class="btn btn-primary">დაწყება</button>
        <button class="btn btn-secondary">გაიგე მეტი</button>
    </div>

    <script>
        // გვერდის ჩატვირთვისთანავე ვრთავთ ანიმაციას
        window.addEventListener('load', () => {
            setTimeout(() => {
                document.getElementById('mainTitle').classList.add('show');
                document.getElementById('actionButtons').classList.add('show');
            }, 300); // 0.3 წამის მერე იწყება მოძრაობა
        });
    </script>

</body>
</html>
