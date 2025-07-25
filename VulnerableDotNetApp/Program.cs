var builder = WebApplication.CreateBuilder(args);

// VULNERABLE: Disable security headers
builder.Services.AddControllers();
builder.WebHost.ConfigureKestrel(options => options.AddServerHeader = true); // Shows server info

var app = builder.Build();

// VULNERABLE: Disable HTTPS redirection and HSTS
app.Use(async (ctx, next) => {
    ctx.Response.Headers.Add("X-Content-Type-Options", "off"); // Disable MIME sniffing protection
    await next();
});

app.MapControllers();
app.Run();